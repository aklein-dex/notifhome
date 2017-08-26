<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type">
</head>
<body>
<div id='main'>
    <h1>Notifhome</h1>
    
    <div class='login_fields' >
        <input id="username" class="login" type="text" name="username" placeholder="username"/>
        <input id="password" class="login" type="password" name="password" placeholder="password"/>
    </div>
    
    <div id='form_create_notif' class="form">
        <h3>Send notification</h3>
        <form id="form_create" action="notification" method="post">
            <p>
                <label>Message</label> 
                <textarea type="text" rows="4" cols="21" name="message"></textarea>
            </p>
            <p>
                <label>Light</label> 
                <input type="radio" name="light" value="1" checked/> On <input type="radio" name="light" value="0"/> Off
            </p>
            <p>
                <label>Sound</label> 
                <input type="radio" name="sound" value="1" checked/> On <input type="radio" name="sound" value="0"/> Off
            </p>
            <button type="submit" style="background-color: #8bc34a">Send</button>
            <div id='status_send' class="status" style='display: none;'><p></p></div>
        </form>
        
    </div>
    
    <div id='form_view_notif' class="form">
        <h3>View notification</h3>
        <form id="form_view" action="view" method="get">
            <button type="submit" style="background-color: #03a9f4">View</button>
            <p>
                <label>Notification</label>
                <textarea id="current_notification" type="text" rows="4" cols="21" name="message"></textarea>
            </p>
            <div id='status_view' class="status" style='display: none;'><p></p></div>
        </form>
    </div>
    
    <div id='form_delete_notif' class="form">
        <h3>Delete notification</h3>
        <form id="form_delete" action="delete" method="post">
            <button type="submit" style="background-color: #f44336">Delete</button>
            <div id='status_delete' class="status" style='display: none;'><p></p></div>
        </form>
    </div>
    
    <br>
    
    <script src="public/jquery.min.js"></script>
    <script>
        // Prevent form submission, send POST asynchronously and parse returned JSON
        $('#form_create').submit(function() {
            $("div#status_send").fadeIn(100);
            $.post($(this).attr('action'), $(this).serialize(), function(j) {
              if (j.ok) {
                $("div#status_send").css("background-color", "#f0fff0");
              } else {
                $("div#status_send").css("background-color", "#fff0f0");
              }
              $("div#status_send p").text(j.msg);
              $("div#status_send").delay(5000).fadeOut(500);
            }, "json");
            return false;
        });
        
        $('#form_view').submit(function() {
            $("div#status_view").fadeIn(100);
            $.get($(this).attr('action'), $(this).serialize(), function(j) {
              if (j.ok) {
                $("div#status_view").css("background-color", "#f0fff0");
              } else {
                $("div#status_view").css("background-color", "#fff0f0");
              }
              $("div#status_view p").text(j.msg);
              $("div#status_view").delay(5000).fadeOut(500);
            }, "json");
            return false;
        });
        
        $('#form_delete').submit(function() {
            if(confirm('Are you sure?')) {
                $("div#status_delete").fadeIn(100);
                $.post($(this).attr('action'), $(this).serialize(), function(j) {
                  if (j.ok) {
                    $("div#status_delete").css("background-color", "#f0fff0");
                  } else {
                    $("div#status_delete").css("background-color", "#fff0f0");
                  }
                  $("div#status_delete p").text(j.msg);
                  $("div#status_delete").delay(5000).fadeOut(500);
                }, "json");
            }
            return false;
        });
    </script>
</div>
<style>
div#commands { width: 45%%; float: left}
div#users { width: 45%; float: right}
div#main {
    color: #777;
    margin: auto;
    margin-left: 5em;
    font-size: 80%;
}

div.form {
    border: 1px solid #777;
    margin: 20px;
    width: 290px;
    padding: 0px 10px 10px 10px;
}

div.login_fields {
    margin: 20px;
}

input.login {
    width: 150px;
}

input {
    background: #f8f8f8;
    border: 1px solid #777;
    margin: auto;
}
input:hover { background: #fefefe}
label {
  width: 8em;
  float: left;
  text-align: right;
  margin-right: 0.5em;
  display: block
}
button {
    margin-left: 13em;
}
button.close {
    margin-left: .1em;
}
div.status {
    padding: 2px;
    margin-top: 10px;
}
.clear { clear: both;}
div#urls {
  position:absolute;
  top:0;
  right:1em;
}
</style>
</body>
</html>
