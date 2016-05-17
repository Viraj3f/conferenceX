function row_to_json(element){
    var attributes = {};

    attributes.id = parseInt(element.getAttribute("row_id"));
    attributes.table = element.getAttribute("table");
    attributes.column = element.getAttribute("column");

    if (element.type === "checkbox") {
        attributes.value = element.checked;
    } else {
        attributes.value = element.value;
    }

    return attributes;
}

function delete_row(element){
    var ary = row_to_json(element);
    ary.delete = true;

    return ary;
}

$(document).ready(function() {
    $(".dynamic-text").change(function() {
        $.ajax({
            type: "POST",
            url: "/admin",
            data: JSON.stringify(row_to_json(event.target)),
            dataType: 'json',
            contentType: 'application/json',
        });
    });

    $(".delete-row").click(function() {
        if (confirm("Delete row? This cannot be undone!")){
            data = delete_row(event.target);
            console.log(data);
            $.ajax({
                type: "POST",
                url: "/admin",
                data: JSON.stringify(data),
                dataType: 'json',
                contentType: 'application/json',
                success: function() {
                    var selector = "div[row_id=" + data.id + "]" +
                                   "[table=" + data.table +  "]";

                    console.log("going to remove" + selector);
                    $(selector).remove();
                },
                error: function(error){
                    alert("There was an internal error");
                }
            });
        }
    });
});