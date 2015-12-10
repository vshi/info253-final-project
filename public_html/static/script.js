/* script.js */

/* When the madlib form is submitted, run this function */
$(document).ready(function(){
   $(".error").hide(); 
    $("a#next").hide(); 
    $(".popup").hide();
});
$("#whosaidthisshit").submit(function() {
    $(".error").hide();
    $("input[type='submit']").hide();
    $("a#next").show();
    var madlibStory = "";
    
    var isOkay = true;
    
    var checked = $("#whosaidthisshit input:checked")
    
    checked.siblings(".error").removeAttr("id")
    checked.siblings(".error").html(checked.val());
    if (checked.val() === "incorrect"){
        checked.siblings(".error").attr("id", "incorrect");
    }
    if (checked.val() === "correct"){
        checked.siblings(".error").attr("id", "correct");
    }
    checked.siblings(".error").show()
    return false;
});
$(".phrase").click(function(){
    
    var phrase = $(this).text();
    var counter = $(".counter#"+phrase);
    var count = parseInt(counter.text());
    count += 1;
    counter.html(count);
    
    var total_count = 0;
    var counters = $(".counter");
    counters.each(function(){
        total_count += parseInt($(this).text());
    })
    if (total_count > 5){
        var popup = $(".popup");
        var warning_message = "You've had " + total_count.toString() + " shots already!";
        $(".popup .warning").html(warning_message);
        popup.show();
    }
});
$("#keep-going").click(function(){
    $(".popup").hide();
});


