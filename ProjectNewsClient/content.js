const default_threshold = 0.25;

let doc = null;
let threshold = default_threshold;
let open = false;

chrome.runtime.onMessage.addListener(
    function(message) {
        if (message.type == "data") {
            popData(message.data);
        }
        if (!open && doc != null && message.type == "showPanel") {
            popValue(); // make sure have the updated value
            showPanel();
        }
        if (message.type == "sliderValue") {
            popValue();
            if (open) {
                closePanel();
                showPanel();
            }
        }
        if (open && message.type == "closePanel") {
            closePanel();
        }
    });

function popValue() {
    chrome.storage.sync.get("slider", function(result) {
        threshold = result.slider / 100;
    });
}

function popData(value) {
    doc = value;
}

function closePanel() {
    $("#unopinionated-reader").remove();
    open = false;
}

function showPanel() {
    $.get(chrome.extension.getURL('/view.html'), (view) => {
        $("body").append(view);
        let cumScore = 0;
        let totalCount = 0;
        for (i = 0; i < doc.sentences.length; i++) {
            let sentence = doc.sentences[i];
            let element = null;
            if (sentence.isBreak) {
                element = '<span><br/><br/></span>';
            } else {
                totalCount++;
                let a = 'good';
                if (sentence.score > threshold) {
                    a = 'bad';
                }
                cumScore += sentence.score;
                element = '<span class="sentence ' + a + '">' + sentence.sentence + ' ' + '</span>';
            }
            if (element != null) {
                $("#reshmiifuchangethisilleatu").append(element);
                $("#articleScore").text("Subjectivity Percentage: " + Math.trunc(cumScore/totalCount*100) + "%");
                open = true;
            }
        }
    });
}