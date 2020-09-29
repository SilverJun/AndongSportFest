function Initialize() {
 
  var triggers = ScriptApp.getProjectTriggers();
 
  for (var i in triggers) {
    ScriptApp.deleteTrigger(triggers[i]);
  }
 
  ScriptApp.newTrigger("onFormSubmitEx")
    .forSpreadsheet(SpreadsheetApp.getActiveSpreadsheet())
    .onFormSubmit()
    .create();
}

function onFormSubmitEx(e) {
  
  var timestamp = e.values[0];
  var email = e.values[1]; // 메일
  var title = e.values[2]; // 제목
  var video = e.values[3]; // 영상
  var images = e.values[4]; // 사진
  var tag = e.values[5]; // 태그
  var serverUrl = "";
  
  var data = {
    'title': title,
    'tag' : tag,
    'video': video,
    'images': images
  };
  
  var options = {
    'method' : 'POST',
    'contentType': 'application/json',
    // Convert the JavaScript object to a JSON string.
    'payload' : JSON.stringify(data)
  };
  
  UrlFetchApp.fetch(serverUrl, options);
}