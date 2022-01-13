const baby = document.getElementById("baby")
const spinnerBox = document.getElementById("spinner-box")


const getCookie=(name)=> {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


const addRemoveSong = ()=> {
    const addRemoveForms = [...document.getElementsByClassName("add-remove-song-forms")]
    addRemoveForms.forEach(form=> form.addEventListener('submit', e=>{
        e.preventDefault()
        const clickedId = e.target.getAttribute('data-form-id')
        const clickedBtn = document.getElementById(`add-remove-song-btn-${clickedId}`)

        $.ajax({
            type: 'POST',
            url: "/add_remove_song/",
            data: {
                'pk': clickedId,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response){
                console.log(response)
                if (response.add_in_pl){
                    clickedBtn.innerText = "Remove" 
                }
                else{
                    clickedBtn.innerText = "Add" 
                }
                // document.getElementById("liked-count").innerText = "added by "+`${response.liked_count}`
            },
            error: function(error){
                console.log(error)
            }
        })
    }))
}


const finalAddSongsPl = ()=> {
    const finalAddSongsForms = [...document.getElementsByClassName("final-add-songs-pl-forms")]
    finalAddSongsForms.forEach(form=> form.addEventListener('submit', e=>{
        e.preventDefault()
        const clickedId = e.target.getAttribute('data-form-id')
        const clickedBtn = document.getElementById(`final-add-songs-pl-btn-${clickedId}`)

        $.ajax({
            type: 'POST',
            url: "/final_add_songs_pl/",
            data: {
                'pl': clickedId,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response){
                console.log(response)
                window.location.replace('/songs/'+clickedId+'/')
            },
            error: function(error){
                console.log(error)
            }
        })
    }))
}


setTimeout(()=>{
    addRemoveSong()
    finalAddSongsPl()
    spinnerBox.classList.add('hide-it')
    baby.classList.remove('hide-it')
},500)