var express = require('express');
var router = express.Router();

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var articleSchema = new Schema({
    url: String,
    sentences: [Object]
});
var Article = mongoose.model('Article', articleSchema);

router.get('/', function(req, res, next) {
    let url = req.query.url;
    Article.findOne({ url })
        .then((doc) => {
            res.send({ error: null, doc });
        })
        .catch((err) => {
            res.send({ error: err });
        })
});

module.exports = router;