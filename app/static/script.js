$(function () {
        $(".demo2").bootstrapNews({
            newsPerPage: 1,
            autoplay: true,
			pauseOnHover:true,
            direction: 'up',
            newsTickerInterval: 4000,
            onToDo: function () {
                //console.log(this);
            }
        });		

    });