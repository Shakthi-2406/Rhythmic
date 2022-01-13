const baby = document.getElementById("baby")
const spinnerBox = document.getElementById("spinner-box")
const songAudio = document.getElementById("song-audio")
const playBtn = document.getElementById("play-btn")
const pauseBtn = document.getElementById("pause-btn")
const progressBar = document.getElementById("progress")
const progressDiv = document.getElementById("progress_div")
const totalTime = document.getElementById("duration").innerText
const music = document.querySelector("audio")
const image = document.querySelector("img")
const NextSongDataClass = document.querySelector(".next-song-playing")
const autoLoopBtn = document.querySelector("#auto-loop-btn")
const quickShortMsg = document.querySelector("#quick-short-msg")
let songPlaying = true
let timeSecond=0
let timeMinute=0
let autoLoop = false


// NECCESSITIES
correctDuration()
songAudio.play()
console.log(totalTime)


// LOADING THINGS
setTimeout(()=>{
    likeUnlikeSongs()
    spinnerBox.classList.add('hide-it')
    baby.classList.remove('hide-it')
},300)


// QUICK-MSG FUNCTION
function quickShortMsgFunc(msg){
    quickShortMsg.innerText = msg
    quickShortMsg.classList.toggle("hide-it") //showing msg

    setTimeout(() => {
        quickShortMsg.classList.toggle("hide-it")
    }, 500);
} 


// AUTO LOOP BUTTON
autoLoopBtn.addEventListener("click",()=>{
    if(autoLoop){
        autoLoop = false
        quickShortMsgFunc("playing all songs")
        autoLoopBtn.innerText = "Loop"
        music.loop = false
    }
    else{
        autoLoop = true
        quickShortMsgFunc("auto repeating current song")
        autoLoopBtn.innerText = "Shuffle"
        music.loop = true
    }
})


// GETTING DATA OF NEXT LINK
if (NextSongDataClass){
    const xxx = NextSongDataClass.id
    NextSongLinkId = xxx.charAt(xxx.length -1)
    NextPLId = xxx.charAt(xxx.length -2)
    console.log(NextSongLinkId)
    console.log(NextPLId)
}


// PLAY AND PAUSE BUTTON
playBtn.addEventListener("click",()=>{
    songAudio.play()
    playBtn.classList.toggle("hide-it")
    pauseBtn.classList.toggle("hide-it")
    progressBar.style.animationPlayState = "running"
    songPlaying = true
    image.classList.toggle("animate-it")
})
pauseBtn.addEventListener("click",()=>{
    songAudio.pause()
    playBtn.classList.toggle("hide-it")
    pauseBtn.classList.toggle("hide-it")
    songPlaying = false
    image.classList.toggle("animate-it")
})


// CURRENT TIME
music.addEventListener("timeupdate", (e) =>{
    const{ currentTime, duration } = e.target
    let progress_time = (currentTime/duration)*100
    progressBar.style.width = `${progress_time}%`

    let currentDurationMinute = Math.floor(currentTime/60)
    let currentDurationSecond = Math.floor(currentTime%60)
    document.getElementById("current_time").textContent = currentDurationMinute+":"+String("0"+currentDurationSecond).slice(-2)
})


// PROGRESS ON CLICK FUNCTIONALITY
progressDiv.addEventListener('click', (e)=>{
    console.log(e)
    const{ duration } = music

    let moveProgress = (e.offsetX / e.target.clientWidth) * duration
    console.log(moveProgress)
    music.currentTime = moveProgress
    console.log("doneee")
})


// PLAYING NEXT SONG IF NOT AUTOLOOP
if(!autoLoop)
{
    music.addEventListener('ended', ()=>{
        console.log("But whyyyyyy")
        if(isNaN(NextPLId) && NextSongLinkId!=0){
            window.location.replace('/songs/detail/'+NextSongLinkId+'/')
        }
        else if(NextSongLinkId!=0){
            window.location.replace('/songs/detail/'+NextSongLinkId+'/'+NextPLId+'/')
            console.log("success")
        }
    })
}


// TOTAL DURATION 
function correctDuration(){
    let correctDurationMinute = Math.floor(totalTime/60)
    let correctDurationSecond = totalTime%60
    document.getElementById("duration").innerText = correctDurationMinute+":"+String("0"+correctDurationSecond).slice(-2)
}


// CSRF TOKEN
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


// LIKE UNLIKE BUTTON
const likeUnlikeSongs = ()=> {
    const likeUnlikeForms = [...document.getElementsByClassName("like-unlike-forms")]
    likeUnlikeForms.forEach(form=> form.addEventListener('submit', e=>{
        e.preventDefault()
        const clickedId = e.target.getAttribute('data-form-id')
        const clickedBtn = document.getElementById(`like-unlike-btn-${clickedId}`)

        $.ajax({
            type: 'POST',
            url: "/like_unlike_song/",
            data: {
                'pk': clickedId,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response){
                console.log(response)
                if (response.liked){
                    clickedBtn.innerText = "Dislike" 
                    quickShortMsgFunc("added to favourites")
                }
                else{
                    clickedBtn.innerText = "Like" 
                    quickShortMsgFunc("removed from favourites")
                }
                document.getElementById("liked-count").innerText = `${response.liked_count}`
            },
            error: function(error){
                console.log(error)
            }
        })
    }))
}


