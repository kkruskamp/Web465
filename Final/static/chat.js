//JS sends message to view
$('#chat-form').on('submit', function(event)
{
  event.preventDefault();

  $.ajax(
    {
      url : '/post/',
      type : 'POST',
      //capture value of submission box
      data : { msgbox : $('#chat-msg').val() },

      success : function(json)
      {
        //empy submission box
        $('#chat-msg').val('');
        //Append to HTML list
        $('#msg-list').append('<li class="text-right list-group-item">' + json.msg + '</li>');
        var chatlist = document.getElementById('msg-list-div');
        chatlist.scrollTop = chatlist.scrollHeight;
      }
    });
  });
  
  // While not scrolling get messages from views
  function getMessages()
  {
    if (!scrolling)
    {
      $.get('/messages/', function(messages)
      {
        $('#msg-list').html(messages);
        var chatlist = document.getElementById('msg-list-div');
        chatlist.scrollTop = chatlist.scrollHeight;
      });
    }
    scrolling = false;
  }

  var scrolling = false;

  $(function()
  {
    // while scrolling messages will not be gotten
    $('#msg-list-div').on('scroll', function()
    {
      scrolling = true;
    });
    //"real time"
    refreshTimer = setInterval(getMessages, 300);
  });

  //disable send button when empty
  $(document).ready(function()
  {
    $('#send').attr('disabled','disabled');
    $('#chat-msg').keyup(function()
    {
      if($(this).val() != '')
      {
        $('#send').removeAttr('disabled');
      }

      else
      {
        $('#send').attr('disabled','disabled');
      }
    });
  });

  // FROM DJANGGO CSRF DOC
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
