var platform = $('#platform');

function dado() {
    platform.removeClass('stop').addClass('playing');
    $('#dice');
    setTimeout(function () {
        platform.removeClass('playing').addClass('stop');
        var letters = ['A', 'B', 'C', 'D', 'E', 'F'];
        var number = Math.floor(Math.random() * 6);
        var x = 0, y = 20, z = -20;
        switch (number) {
            case 0:
                x = 0;
                y = 20;
                z = -20;
                break;
            case 1:
                x = -100;
                y = -150;
                z = 10;
                break;
            case 2:
                x = 0;
                y = -100;
                z = -10;
                break;
            case 3:
                x = 0;
                y = 100;
                z = -10;
                break;
            case 4:
                x = 80;
                y = 120;
                z = -10;
                break;
            case 5:
                x = 0;
                y = 200;
                x = 10;
                break;
        }

        $('#dice').css({
            'transform': 'rotateX(' + x + 'deg) rotateY(' + y + 'deg) rotateZ(' + z + 'deg)'
        });

        platform.css({
            'transform': 'translate3d(0,0, 0px)'
        });

        $('#outcome').text(letters[number]);

    }, 1120);
}