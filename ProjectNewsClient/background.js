var supportedSitesRule = {
    conditions: [
        new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { hostEquals: 'www.bbc.com' },
        }),
        new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { hostEquals: 'www.foxnews.com' },
        }),
        new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { hostEquals: 'www.nytimes.com' },
        }),
        new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { hostEquals: 'www.cnn.com' },
        }),
    ],
    actions: [new chrome.declarativeContent.ShowPageAction()]
};

chrome.runtime.onInstalled.addListener(function(details) {
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
        chrome.declarativeContent.onPageChanged.addRules([supportedSitesRule]);
    });
    chrome.storage.sync.set({ "slider": 25 });
});