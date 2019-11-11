let received = false;
let doc = null;
let tab = "";
let sliderNumb = 50;

chrome.tabs.query({ 'active': true, 'lastFocusedWindow': true }, function(tabs) {
    let currentUrl = tabs[0].url;
    let reqUrl = "https://projectnews-258608.appspot.com/article";
    $.get(reqUrl, { url: currentUrl }, (response) => {
        received = true;
        if (response.error == null && response.doc != null) {
            doc = response.doc;
            tab = tabs[0].id; // uh leave this
            chrome.tabs.sendMessage(tab, { type: "data", data: doc });
        } else {
            $("#actions").remove();
            $("#message").text("Article Not Found");
        }
    });
});

function init() {
    document.getElementById('process').addEventListener('click', getSidePanel);
    document.getElementById('close').addEventListener('click', closeSidePanel);
    document.getElementById('set').addEventListener('click', setValue);
    chrome.storage.sync.get("slider", function(result) {
        document.getElementById("slider").value = result.slider;
        document.getElementById("value").innerText = (result.slider + "%");
    });
    document.getElementById("slider").oninput = function() {
        document.getElementById("value").innerText = (this.value + "%");
        sliderNumb = this.value;
    }
}

document.addEventListener('DOMContentLoaded', init);

function setValue() {
    chrome.storage.sync.set({ "slider": sliderNumb }, function() {
        chrome.tabs.query({ 'active': true, 'lastFocusedWindow': true }, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { type: "sliderValue", value: sliderNumb });
        });
    });
}

function getSidePanel() {
    chrome.tabs.query({ 'active': true, 'lastFocusedWindow': true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { type: "showPanel" });
    });
}

function closeSidePanel() {
    chrome.tabs.query({ 'active': true, 'lastFocusedWindow': true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { type: "closePanel" });
    });
}