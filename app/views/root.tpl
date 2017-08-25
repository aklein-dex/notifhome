<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type">
</head>
<body>
<div id='main'>
    <h1>Notifhome</h1>
    
    <div id='status' style='display: none;'><p></p></div>
    
    <input id="username" type="text" name="username" placeholder="username"/>

    <input id="password" type="password" name="password" placeholder="password"/>

    <div id='form_create_notif'>
        <h3>Send notification</h3>
        <form id="form_create" action="notification" method="post">
            <p>
                <label>Message</label> 
                <input type="text" name="message" />
            </p>
            <p>
                <label>Light</label> 
                <input type="radio" name="light" value="1" checked/> On <input type="radio" name="light" value="0"/> Off
            </p>
            <p>
                <label>Sound</label> 
                <input type="radio" name="sound" value="1" checked/> On <input type="radio" name="sound" value="0"/> Off
            </p>
            <button type="submit" >Send</button>
        </form>
        
    </div>
    
    <div id='form_view_notif'>
        <h3>View notification</h3>
        <form id="form_view" action="view" method="get">
            <button type="submit" >View</button>
        </form>
    </div>
    
    <div id='form_delete_notif'>
        <h3>Delete notification</h3>
        <form id="form_delete" action="delete" method="post">
            <button type="submit" >Delete</button>
        </form>
    </div>
    
    <br>
    
    <script src="public/jquery.min.js"></script>
    <script>
        // Prevent form submission, send POST asynchronously and parse returned JSON
        $('#form_create').submit(function() {
            $("div#status").fadeIn(100);
            $.post($(this).attr('action'), $(this).serialize(), function(j) {
              if (j.ok) {
                $("div#status").css("background-color", "#f0fff0");
              } else {
                $("div#status").css("background-color", "#fff0f0");
              }
              $("div#status p").text(j.msg);
              $("div#status").delay(5000).fadeOut(500);
            }, "json");
            return false;
        });
        
        $('#form_view').submit(function() {
            $("div#status").fadeIn(100);
            $.get($(this).attr('action'), $(this).serialize(), function(j) {
              if (j.ok) {
                $("div#status").css("background-color", "#f0fff0");
              } else {
                $("div#status").css("background-color", "#fff0f0");
              }
              $("div#status p").text(j.msg);
              $("div#status").delay(5000).fadeOut(500);
            }, "json");
            return false;
        });
        
        $('#form_delete').submit(function() {
            if(confirm('Are you sure?')) {
                $("div#status").fadeIn(100);
                $.post($(this).attr('action'), $(this).serialize(), function(j) {
                  if (j.ok) {
                    $("div#status").css("background-color", "#f0fff0");
                  } else {
                    $("div#status").css("background-color", "#fff0f0");
                  }
                  $("div#status p").text(j.msg);
                  $("div#status").delay(5000).fadeOut(500);
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
div#status {
    border: 1px solid #999;
    padding: .5em;
    margin: 2em;
    width: 15em;
    -moz-border-radius: 10px;
    border-radius: 10px;
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
