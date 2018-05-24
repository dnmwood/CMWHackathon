function search(words) {
  var snd = new Audio("audio/graph2.wav");
  snd.play();

  // var count = 0
  // var bandList = []
  // var band1 = "name: 'Good Kid', song: 'Hot Fire', genre: 'Indie'"
  // var band2 = "name: 'Ivory Hours', song: 'Goosebumps LoL', genre: 'Rock'"
  // var band3 = "name: 'Monowhale', song: 'Toronto is fucking #life #TO #homeiswherethefartis', genre: 'Stupid'"
  // var band4 = "name: 'Voxtrott', song: 'Start of Something', genre: 'Indie'"
  // var band5 = "name: 'Wolfgang', song: 'Oldie', genre: 'Hip Hop'"
  // var band6 = "name: 'Shad', song: 'The Old Prince Still Lives at Home', genre: 'Hip Hop'"
  // var band7 = "name: 'Shad', song: 'The Old Prince Still Lives at Home', genre: 'Hip Hop'"
  // var band8 = "name: 'Shad', song: 'The Old Prince Still Lives at Home', genre: 'Hip Hop'"
  // var band9 = "name: 'Shad', song: 'The Old Prince Still Lives at Home', genre: 'Hip Hop'"
  // var band10 = "name: 'Shad', song: 'The Old Prince Still Lives at Home', genre: 'Hip Hop'"
  // bandList.push(band1, band2, band3, band4, band5, band6, band7, band8, band9, band10)

  // for (i = 0; i < words.length; i++) {
  //   console.log(words[i])
  // }
  //
  // for (i = 0; i < bandList.length; i++) {
  //   if (bandList[i].includes(words[0])) {
  //     var count = count + 1
  //   }
  // }

  // console.log("count:", count )
  // var height = (count * 100.0 / 10)
  // $(".graphBarOne").css("height", height)
  //
  // if ( words[0] == "Hot" && words[1] == "Fire" ) {
  //   console.log("Dylan")
  //   console.log("Dylan")
  //   console.log("Dylan")
  //   console.log("Dylan")
  //   console.log("Dylan")
  //   console.log("Because I spit hot fiya")
  // }
}

function getGenres(obj) {
  console.log(obj)
}

$(function() {
  $( 'form' ).submit(function(e) {
    e.preventDefault();
    var srcString = $('.search-bar').val();
    var words = srcString.split(" ");
    search(words);
  });
})
