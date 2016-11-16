$.b_alert = function (message) {
    if ($('#my-modal-container').length == 0) {
        var container = $.here_doc(function () {
            /*
             <div class="modal fade" id="my-modal-container" tabindex="-1" role="dialog" aria-labelledby="my-modal-title" aria-hidden="true">
             <div class="modal-dialog">
             <div class="modal-content">
             <div class="modal-header">
             <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
             <h4 class="modal-title" id="my-modal-title"></h4>
             </div>
             <div class="modal-body"></div>
             </div>
             </div>
             </div>
             */
        });
        $("body").append(container);
    }
    if(message && message.length){
        $('#my-modal-container .modal-body').html(message);
        $('#my-modal-container').modal('show');
    }
};

$.here_doc = function (fn) {
    return fn.toString().split('\n').slice(1, -1).join('\n') + '\n';
};