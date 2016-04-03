var request = require('requestretry');
var querystring = require('querystring');
var config = require('../../config.json');
module.exports = function(Device) {

  //Remote Hooks

  //Add the Device Name property
  Device.beforeRemote('*', function(ctx, user, next) {
    var body = ctx.req.body;
    if (body && body.deviceName) {
        body.email = body.deviceName+'@cutranspo.com';
      }
    return next();
  });

  // Remove the email from from each call
  Device.afterRemote('*', function (ctx, user, next) {
    if(ctx.result) {
      delete ctx.result.email;
    }
    return next();
  });

  Device.beforeRemote('create', function(ctx, user, next) {
    var body = ctx.req.body;
    if (!body || !body.deviceName || !body.stopNo) {
      return next(new Error('Parameters Not given'));
    }
    else {
      body.requestHits = 0;
      console.log('Device created: ', body.email);
    }
    return next();
  });

  Device.beforeRemote('login', function(ctx, user, next) {
    ctx.req.body.ttl = 182000;
    return next();
  });

  //Remote Methods
  Device.getTimes = function(next) {
    Device.find({
      where:{
        id:Device.app.currentUserId
      },
      fields: ['stopNo']
    },function(err, modelData){
      console.log(modelData);

      pollOCTranspo(modelData[0].stopNo,function(err,data){
          return next(null,{
            success: err ? false : true,
            data: data
          });
      });//call function
    });//find busNo based on device connected
  };//end remote method


  Device.setup = function () {
    Device.remoteMethod('getTimes',{
      returns: {arg: 'response', type: 'Object'},
      http: {path:'/getTimes', verb: 'get'}
    });

    Device.disableRemoteMethod('upsert', true);
    Device.disableRemoteMethod('updateAll', true);
    Device.disableRemoteMethod('updateAttributes', false);
    Device.disableRemoteMethod('find', true);
    Device.disableRemoteMethod('findById', true);
    Device.disableRemoteMethod('findOne', true);
    Device.disableRemoteMethod('deleteById', true);
    Device.disableRemoteMethod('confirm', true);
    Device.disableRemoteMethod('count', true);
    // Device.disableRemoteMethod('exists', true);
    Device.disableRemoteMethod('resetPassword', true);
    Device.disableRemoteMethod('change-stream', true);
    Device.disableRemoteMethod('__count__accessTokens', false);
    Device.disableRemoteMethod('__create__accessTokens', false);
    Device.disableRemoteMethod('__delete__accessTokens', false);
    Device.disableRemoteMethod('__destroyById__accessTokens', false);
    Device.disableRemoteMethod('__findById__accessTokens', false);
    Device.disableRemoteMethod('__get__accessTokens', false);
    Device.disableRemoteMethod('__updateById__accessTokens', false);
  };

  Device.setup();
};



function pollOCTranspo (stopNo, next) {
  request({
    method: 'POST',
    uri: 'https://api.octranspo1.com/v1.2/GetNextTripsForStopAllRoutes',
    form:{
      appID: config.ocTranspo.appID,
      apiKey: config.ocTranspo.apiKey,
      stopNo: stopNo,
      format:'json'
    },
    json: true
  }, function(err, response, body) {
    if(err){
      return next(err,err);// return
    }
    var result = {};
    if(body &&
    body.GetRouteSummaryForStopResult &&
    body.GetRouteSummaryForStopResult.Routes &&
    body.GetRouteSummaryForStopResult.Routes.Route) {

      body.GetRouteSummaryForStopResult.Routes.Route.forEach(function(route){
        var dest = route.RouteHeading;
        if (!Array.isArray(result[route.RouteNo])) {
          result[route.RouteNo] = [];
        }
        result[route.RouteNo].push({
          'dest': dest,
          'times':getTrips(route)
        });
      });

      return next(null,result);//return
    }
    else {
      return next(true,'No Routes Available');
    }
  });//get request
}// poll OC Transpo

function getTrips(route) {
  var trips = [];

  console.log(route);
  if(typeof route.Trips === 'object') {
    if (Array.isArray(route.Trips)) {
      route.Trips.forEach(function(trip) {
        trips.push(trip.TripStartTime);
      });
    }
    else {
      trips.push(route.Trips.TripStartTime);
    }
  }
  return trips;
}
