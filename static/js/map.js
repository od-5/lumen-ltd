// 
// $(function(){
ymaps.ready(init);
var myMap;

function init(){
    city = 'Москва';
    var coord = ''
    var myGeocoder = ymaps.geocode(city);
        myGeocoder.then(
            function (res) {
                coord = res.geoObjects.get(0).geometry.getCoordinates();
                myMap = new ymaps.Map("YMapsID", {
                    center: coord,
                    zoom: 4
                });
                $.get("/map/",
                    function(e) {
                        //var data = JSON.parse(e); // получаем данные от сервера
                        //console.log(e);
                        function outputItem(item, i, e) {
                            myMap.geoObjects.add(
                                new ymaps.Placemark([item['coord_y'], item['coord_x']], {
                                balloonContent: item['name'],
                                hintContent: item['name']
                                })
                            );
                        }
                        e.forEach(outputItem);
                    }
                );


            }
            //function (err) {
            //    coord = [48.707103, 44.516939];
            //    myMap = new ymaps.Map("YMapsID", {
            //        center: coord,
            //        zoom: 11
            //    });
            //    $.get("/map/",
            //        function(e) {
            //            //var data = JSON.parse(e); // получаем данные от сервера
            //            //console.log(e);
            //            function outputItem(item, i, e) {
            //                myMap.geoObjects.add(
            //                    new ymaps.Placemark([item['coord_y'], item['coord_x']], {
            //                    balloonContent: item['address'],
            //                    hintContent: item['name']
            //                    })
            //                );
            //            }
            //            e.forEach(outputItem);
            //        }
            //    );
            //}
        );
    //console.log(coord);
    //myMap = new ymaps.Map("YMapsID", {
    //    center: coord,
    //    zoom: 11
    //});
    //console.log(ymaps.geocode('Волгоград', { results: 1 }));


}