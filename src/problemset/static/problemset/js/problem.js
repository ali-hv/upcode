try {
    var tab = window.location.href.split('?')[1].split('=')[1]
}
catch (err) {
    document.getElementById("problem-tab").click();
}

if (tab === "submission")
    document.getElementById("submission-tab").click();
else
    document.getElementById("problem-tab").click();

function openSection(evt, tabName) {
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
    }

    document.querySelector("#choosefile").onchange = function(){
      let filename = document.querySelector("#choosefile").textContent = this.files[0].name;
      document.getElementById('filename-label').innerHTML = filename;

      let submit = document.getElementById('submit');
      submit.style.opacity = '100%';
      submit.style.cursor = 'pointer';
      submit.onmouseover = function()
        {
            this.style.backgroundColor = "#ee4ae2";
        }
      submit.onmouseleave = function()
        {
            this.style.backgroundColor = "#ee13df";
        }
    }

function getLanguage() {
    var languageName = document.getElementById("languageSelect");
    var name = languageName.options[ languageName.selectedIndex ].value;

    var languageInput = document.getElementById('languageName');
    languageInput.value = name;

    return true;
}

function openJudgeResult(submission_id) {
    document.getElementById('judge-result-'+submission_id).style.display='block';
}

function closeJudgeResult(submission_id) {
    document.getElementById('judge-result-'+submission_id).style.display='none';
}

function openSourceCode(submission_id) {
    document.getElementById('source-code-'+submission_id).style.display = 'block';
}

function closeSourceCode(submission_id) {
    document.getElementById('source-code-'+submission_id).style.display = 'none';
}