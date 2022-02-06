//noteLast();

//csrf token
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

//Render All title

document.getElementsByClassName('leaftag');
noteTitle = document.getElementById('notetitle');
noteRender();

function noteRender() {
  noteTitle.innerHTML = '';
  let url = 'http://127.0.0.1:8000/api/note-list';

  fetch(url)
    .then((response) => response.json())
    .then(function (data) {
      let noteList = data;

      for (let i in data) {
        let item = `
                    <h6>${data[i].note_title}</h6> <hr/>
              `;

        noteTitle.innerHTML += item;
      }
    });
}

function noteLast() {
  console.log('apel mahmud');
  let url = 'http://127.0.0.1:8000/api/note-last/';

  fetch(url)
    .then((response) => response.json())
    .then(function (data) {
      console.log(data['note_title']);
      let h = document.createElement('h6');
      h.textContent = data['note_title'];
      let hr = document.createElement('hr');
      h.append(hr);

      noteTitle.prepend(h);
    });
}

//checkbox access
let chekbox = document.getElementsByClassName('chekbox');
let chekTagName = document.getElementById('checkbox-select');
let formClear = document.getElementById('formclear');
let chekArr = [];
let checkName = [];

function clk() {
  chekArr = [];
  checkName = [];
  chekTagName.innerHTML = '<spant>Tags: </span>';
  let item = '';
  for (let i = 0; i < chekbox.length; i++) {
    if (chekbox[i].checked) {
      chekArr.push(parseInt(chekbox[i].value));
      let tempName = chekbox[i].name;
      checkName.push(tempName);
      item += ` <span> ${tempName} </span> `;
    }
  }
  chekTagName.innerHTML += item;
  // console.log('raw javascript', chekArr);
}

// for (let i = 0; i < chekbox.length; i++) {
//   chekbox[i].addEventListener('click', function () {});
// }
// clear all check box after form submit
function clearCheck() {
  for (let i = 0; i < chekbox.length; i++) {
    if (chekbox[i].checked) {
      chekbox[i].checked = false;
    }
  }
  chekTagName.innerHTML = '<span>Tags :</span>';
  document.getElementById('form').reset();
}

formclear.addEventListener('click', function () {
  clearCheck();
});

//note saved
let form = document.getElementById('form');

form.addEventListener('submit', function (e) {
  e.preventDefault();
  //  console.log('form submited');
  let url = 'http://127.0.0.1:8000/api/note-create/';
  let title = document.getElementById('titleid').value;
  let subject = document.getElementById('subjectid').value;

  // console.log(title, subject);

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
      note_title: title,
      note_subject: subject,
      leaf_tag: chekArr,
    }),
  }).then(function (response) {
    noteLast();
    // noteRender();
    clearCheck();
  });
});
