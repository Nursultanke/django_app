
$(document).ready(function () {

    // var NameVars = $('.name-class');

    // // Маска для телефонов
    // if (NameVars !== undefined && NameVars !== null) {
    //     NameVars("(+996) 000-00-00-00");
    // }
    $('.article-text').readmore({
        collapsedHeight: 100,
        embedCSS: false,
        moreLink: '<a href="#" class="show-more">Читать далее<i class="fa fa-chevron-down"></i></a>',
        lessLink: '<a href="#" class="show-more">Закрыть<i class="fa fa-chevron-up"></i></a>'
    });
}); // end document.ready


// $(document).ajaxComplete(loadCommon);
//     $(function () { loadCommon(); });

//     function loadCommon() {
//         // Писать common.js скрипты сюда
//     }

