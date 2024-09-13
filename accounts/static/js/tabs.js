function showTab(tabId) {
    var i, tabcontent, tabbuttons;
    tabcontent = document.getElementsByClassName("tab-content");
    tabbuttons = document.getElementsByClassName("tab-button");

    // Hide all tab content
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove active class from all tab buttons
    for (i = 0; i < tabbuttons.length; i++) {
        tabbuttons[i].classList.remove("active");
    }

    // Show the current tab content and add active class to the current button
    document.getElementById(tabId).style.display = "block";
    document.querySelector('.tab-button[onclick="showTab(\'' + tabId + '\')"]').classList.add("active");
}

// Default open tab
document.addEventListener('DOMContentLoaded', function() {
    showTab('profile-info');
});
