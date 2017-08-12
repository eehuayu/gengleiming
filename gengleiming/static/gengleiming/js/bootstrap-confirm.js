$(function () {
    $.extend({
        alert: function (msg) {
            if ($("#system_confirm_34956").length == 0) {
                var html =
                    "<div id='system_confirm_34956' tabindex='-1' class='modal fade' role='dialog' aria-labelledby=''>" +
                    "<div class='modal-dialog'><div class='modal-content'>" +
                    "<div class='modal-body text-center'>" + msg + "</div>" +
                    "</div></div>" +
                    "</div>";

                $("body").append(html);
            }

            $("#system_confirm_34956").modal("show");
        }
    });
})

