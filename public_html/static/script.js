/* script.js */

/* When the madlib form is submitted, run this function */
$(document).ready(function(){
   $(".error").hide(); 
    $("a#next").hide(); 
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

    
//    var nameInput = $("#madlibForm input[name='name']");
//    var nameValue = "";
//    var partnerInput = $("#madlibForm #partner");
//    var partnerValue = partnerInput.val();
//    var partnerNickname = partnerInput.children("option:selected").text();
//    var cast = [];
//    partnerInput.children("option").each(function(){
//        cast.push($(this).val()); 
//    });
//    var missionsInput = $("#madlibForm input[name='games']");
//    var missions = [];
//
//    var teamInput = $("#madlibForm input[name='team-size']");
//    var numTeams = teamInput.val();
//    var spyInput = $("#madlibForm input[name='spy']");
//    var isSpy = "";
//    
//    if(nameInput.val() === ""){
//        isOkay = false;
//        nameInput.siblings(".error").replaceWith('<div class="error">Fill in your name.</div>')
//        nameInput.siblings(".error").show();
//    }else{
//        nameValue = nameInput.val();
//        cast.push(nameValue);
//    }
//    
//    if(partnerValue === ""){
//        isOkay = false;
//        partnerInput.siblings(".error").replaceWith('<div class="error">Choose a partner.</div>')
//        partnerInput.siblings(".error").show();     
//    }
//    
//    if(missionsInput.filter(":checked").length == 0){
//        isOkay = false;
//        $(".checkbox-container").siblings(".error").replaceWith('<div class="error">Check at least one mission.</div>');
//        $(".checkbox-container").siblings(".error").show();
//    }else{
//        missionsInput.filter(":checked").each(function(){
//           missions.push($(this).val());
//        });
//    }
//
//    if (spyInput.filter(":checked").length == 0){
//        isOkay = false;
//        spyInput.siblings(".error").replaceWith('<div class="error">Choose either a regular or spy game.</div>')
//        spyInput.siblings(".error").show();      
//    }else{
//        isSpy = spyInput.filter(":checked").val();
//    }
//    
//    
//    if(numTeams === "") {
//        isOkay = false;
//        teamInput.siblings(".error").replaceWith('<div class="error">Fill in how many teams you want.</div>')
//        teamInput.siblings(".error").show();
//    } else if(numTeams > 4) {
//        isOkay = false;
//        teamInput.siblings(".error").replaceWith('<div class="error">There cannot be more than 4 teams.</div>')
//        teamInput.siblings(".error").show();
//    } else if (numTeams < 1){
//        isOkay = false;
//        teamInput.siblings(".error").replaceWith('<div class="error">There must be at least one team.</div>')
//        teamInput.siblings(".error").show();    
//    }else{
//        
//    }
//
//    if (isOkay){
//        madlibStory = "<p>Welcome to Running Man!";
//        madlibStory += "  You, " + nameValue + " , and " + partnerValue + ", aka " + partnerNickname + ", are the main characters in today's game.";
//        var gameString = "";
//        gameString += " The missions for today's episode are ";
//        for (i = 0; i < missions.length; i++) { 
//            if (i == missions.length - 1){
//                gameString += "and ";
//                gameString += missions[i];
//                gameString += ".";
//            }else{
//                gameString += missions[i];
//                gameString += ", ";
//            }
//        }
//        madlibStory += gameString;
//        var teamString = "";
//        teamString += "</p><p>The producer announces the teams for today's show. ";
//        var teamList = generateTeams(parseInt(numTeams), cast);
//        for(i = 0; i < teamList.length; i++){
//            teamString += "Team " + (i + 1).toString() + " has members ";
//            for(j = 0; j < teamList[i].length; j ++){
//                if ( j == teamList[i].length - 1){
//                    teamString += "and ";
//                    teamString += teamList[i][j];
//                    teamString += ". ";
//                }else{
//                    teamString += teamList[i][j];
//                    teamString += ", ";                
//                }
//            }
//        }
//        madlibStory += teamString;
//        madlibStory += "</p>";
//        
//        var winners = {};
//        plotString = "<p>";
//        var winningTeamNumber = 0;
//        for (i = 0; i < missions.length; i++) { 
//            winningTeamNumber = Math.floor(Math.random() * teamList.length)
//            plotString += "Team " + (winningTeamNumber + 1).toString() + " wins at " + missions[i] + ". ";
//            if (winners[(winningTeamNumber + 1).toString()] == undefined){
//                winners[(winningTeamNumber + 1).toString()] = 1;
//            }else{
//                winners[(winningTeamNumber + 1).toString()] = winners[(winningTeamNumber + 1).toString()] + 1;
//            }
//        }
//
//        madlibStory += plotString;
//        madlibStory += "</p>";
//        
//        madlibStory += "<p>";
//        madlibStory += "Team " + findWinner(winners) + " is the winner!";
//        madlibStory += "</p>";
//        
//        if(isSpy == "yes"){
//            madlibStory += "<p>";
//            var spyString = "";
//            spyString += "However, little did the cast members know that today's episode was a spy episode!";
//            var spyNumber = Math.floor(Math.random() * cast.length);
//            spyString += " It turns out that the spy was " + cast[spyNumber] + " all along.";
//            
//            var spyWin = Math.floor(Math.random() * 3);
//            if (spyWin === 0){
//                spyString += " Shockingly, " + cast[spyNumber] + " succeeded at their secret mission and won the game.";
//            }else{
//                spyString += " But " + cast[spyNumber] + " was found out, and ousted by the rest of the members.";
//            }
//            madlibStory += spyString;
//            madlibStory += "</p>";
//        }
//        $("#madlibStory").html(madlibStory);
//    }else{
//        $("#madlibStory").html("");
//    }
    /* If all validations pass, add the story to the page */
    
    
    /* Don't load a new page after clicking submit */
    return false;
});




