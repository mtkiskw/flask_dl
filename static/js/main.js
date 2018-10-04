function Download1(){
    $.ajax({
        url: "/download",
        type: "post",
        data: JSON.stringify({"hoge": "hoge"}),
        success: function(data) {
            console.log(data);
            var url = data["url"];
            // var content = "ファイルの中身";
            var link = document.createElement( 'a' );
            link.href = "/getfile/" + url
            // link.href = window.URL.createObjectURL( new Blob( [content] ) );
            // link.download = "filename.csv";
            link.click();
        }
    });

}
