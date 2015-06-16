openerp.pos_receipt_company_logo = function(instance){
    var module = instance.point_of_sale
    pos_company_fields(instance,module);

    function pos_company_fields(instance,module){
        var models = module.PosModel.prototype.models;
         _.each(models,function(model){
            if (model.model == 'res.company'){
                field_values = ['logo']
                model.fields = model.fields.concat(field_values);
            }
         });
    };
};