$(document).ready(function() {
    getQuote();
    $('.quote-btn').click(getQuote);

    function getQuote() {
        $.ajax({
            url: 'http://quotable.io/random',
            dataType: 'json',
            success: function(data){
                const content = data.content;
                const author = data.author;

                $('.quote').text(content);
                $('.author').text(author);
            }
        })
    }
});
