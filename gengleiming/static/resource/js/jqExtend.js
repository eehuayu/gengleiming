$.confirm = function (data, fn) {
    if ($('#my-modal-container').length == 0) {
        var container = $.here_doc(function () {
            /*
             <div class="modal fade" id="my-modal-container" tabindex="-1" role="dialog" aria-labelledby="my-modal-title" aria-hidden="true">
             <div class="modal-dialog">
             <div class="modal-content">
             <div class="modal-header">
             <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
             <h4 class="modal-title" id="my-modal-title">信息</h4>
             </div>
             <div class="modal-body" id="my-modal-body"></div>
             <div class="modal-footer">
             <button type="button" class="btn btn-primary" data-dismiss="modal" id="my-modal-footer">确认</button>
             </div>
             </div>
             </div>
             </div>
             */
        });
        $("body").append(container);
        // $()
    }
    if(typeof(data) == "string"){
        $('#my-modal-container .modal-body').html(data);
    }else if(typeof(data) == "object"){
        if(data.title){
            $("#my-modal-container .modal-header h4").html(data.title);
        }
        if(data.message){
            $("#my-modal-container .modal-body").html(data.message);
        }
    }
    $('#my-modal-container').modal('show');
    if(fn && typeof(fn) == "function"){
        $("#my-modal-container .modal-footer #my-modal-footer").off();
        $("#my-modal-container .modal-footer #my-modal-footer").on("click", fn);
    }
};

$.here_doc = function (fn) {
    return fn.toString().split('\n').slice(1, -1).join('\n') + '\n';
};