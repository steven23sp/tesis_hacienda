$(function () {
    var datatable = $("#example1").DataTable({
        autoWidth: false,
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<span>' + data + '</span>';
                }
            }
        ],
        createdRow: function (row, data, dataIndex) {
            console.log(data);
            if (data[4] === 'ACTIVO') {
                $('td', row).eq(4).find('span').addClass('badge badge-primary');
            } else if (data[4] === 'INACTIVO') {
                $('td', row).eq(4).find('span').addClass('badge badge-danger');
            }

        }

    });

    $('#example1 tbody').on('click', 'a[rel="estado"]', function () {
        var tr = datatable.cell($(this).closest('td, li')).index();
        var data = datatable.row(tr.row).data();
        var parametros = {'id': data['0']};
        save_estado('Alerta',
            '/cantero/estado', 'Esta seguro que desea cambiar el estado de este cantero?', parametros,
            function () {
                menssaje_ok('Exito!', 'Exito en la actualizacion', 'far fa-smile-wink', function () {
                    location.reload();
                });
            });
    });
});

