var app = new Vue({
    el: '#app',
    delimiters:['{$','$}'],
    data: {
      message: 'Hello Vue!',
      saludo:'Hola a todos',
      contador:5,
    },
    methods:{
      del:function(id,num){

        Swal.fire({
          title: '¿Estás seguro?',
          text: "estos cambios no serán reversibles!",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'si, borrar!',
          cancelButtonText:"Cancelar"
        }).then((result) => {
          if (result.isConfirmed) {
            if(num==2){
              window.location.href=`http://209.90.232.169:8082/inventario/libroDelete/${id}`;


            }else{
              window.location.href=`http://209.90.232.169:8082/inventario/autorDelete/${id}`;
            }

        

            Swal.fire(
              'Eliminado!',
              'Los archivos han sido eliminados.',
              'success'
            )
          }
        })

        //console.log("Se preciono el boton borrar");



      },

      form:()=>{

        console.log("Agregar un nuevo usuario");

        $('#modalForm').modal('show');



      }
    }
  })