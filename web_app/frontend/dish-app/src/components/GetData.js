const getData=({ country })=>{

    var country_name = {country.name} + '.json'
    fetch(country_name

    ,{

      headers : { 

        'Content-Type': 'application/json',

        'Accept': 'application/json'

       }

    }

    )

      .then(function(response){

        console.log(response)

        return response.json();

      })

      .then(function(myJson) {

        console.log(myJson);

      });

  }

  useEffect(()=>{

    getData()

  },[])