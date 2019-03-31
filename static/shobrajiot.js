function sendmessage() {
    var messagetitle = document.getElementById('messagetitle').value
    var messagebody = document.getElementById('messagebody').value
    console.log(JSON.parse(messagetitle, messagebody))
    alert(JSON.parse(messagetitle, messagebody))

  }