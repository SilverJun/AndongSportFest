function onFormSubmitEx(e) {
  var timestamp = e.values[0];
  var email = e.values[1]; // 메일
  var title = e.values[2]; // 제목
  var video = e.values[3]; // 영상
  var images = e.values[4]; // 사진
  var serverUrl = "";
  
  var data = {
    'title': title,
    'video': video,
    'imagese': images
  };
  
  var options = {
    'method' : 'POST',
    'contentType': 'application/json',
    // Convert the JavaScript object to a JSON string.
    'payload' : JSON.stringify(data)
  };
  
  UrlFetchApp.fetch(serverUrl, options);
}