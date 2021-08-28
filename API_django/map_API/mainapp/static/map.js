let mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(37.300538, 126.838613), // 지도의 중심좌표
        level: 4 // 지도의 확대 레벨 
    }; 
// 지도를 생성합니다    
let map = new kakao.maps.Map(mapContainer, mapOption);
let markerPosition = new kakao.maps.LatLng(37.300538, 126.838613);
let marker = new kakao.maps.Marker({
    position : markerPosition
}).setMap(map);
let infowindow = new kakao.maps.InfoWindow({zIndex:1});



for (var i=0; i<list_name.length; i++) {
    markerPosition = new kakao.maps.LatLng(list_lat[i], list_lon[i]);
    marker = new kakao.maps.Marker({
        position : markerPosition
    })
    marker.setMap(map);

    (function(marker, title) {
        kakao.maps.event.addListener(marker, 'mouseover', function() {
            displayInfoWindow(marker, title);
        });
        kakao.maps.event.addListener(marker, 'mouseout', function() {
            infowindow.close();
        })
    })(marker, list_name[i]);
}

function displayInfoWindow(marker, title) {
    var content = '<div style="padding:5px;">'+ title + '</div>';
    infowindow.setContent(content);
    infowindow.open(map, marker)
}

