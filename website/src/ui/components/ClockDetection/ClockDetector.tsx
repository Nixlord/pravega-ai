import React from "react";


interface ClockState {

}
export default class ClockDetector extends React.Component<{}, ClockState> {
    render() {
        return <div>Build Clock Detector</div>
    }
}

//
// export default class ClockDetector extends React.Component<{}, ClockState> {
//     state: ClockState = {}
//
//     obviouslyNotWorkingLogic() {
//         const fileField = document.getElementById('inputImageUpload');
//         const textClockTime = document.getElementById('textClockTime');
//
//         // https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#Uploading_a_file
//         const formData = new FormData()
//         formData.append('clock_image', fileField.files[0])
//
//         fetch("/api/upload-clock", {
//             method: "POST",
//             body: formData
//         })
//             .then(res => res.json())
//             .then(json => {
//                 console.log(`Recieved: ${json.hours} : ${json.minutes}`);
//                 textClockTime.appendChild(
//                     document.createTextNode(
//                         `${json.hours} : ${json.minutes}`
//                     )
//                 )
//             })
//     }
//
//     nonWorkingRender() {
//         return (
//             <div className="wrapper">
//                 <div>
//                     <section className="file">
//                         <form action="#" method="post">
//                             <label>
//                                 Enter Image URL:
//                                 <input type="url" name="textline"
//                                        placeholder="E.g. http://www.example.com/example.jpg"/>
//                             </label>
//                             <label>
//                                 Upload from local
//                                 <input type="file" name="datafile" size={40}/>
//                             </label>
//                             <div>
//                                 <input type="submit" value="Upload" id="buttonImageUpload"
//                                        className="submitButton"/>
//                             </div>
//                         </form>
//                     </section>
//                 </div>
//                 <section className="container">
//                     <div className="showcase">
//                         <a href="#" className="img"/>
//                     </div>
//                     <div className="time-box">
//                         <h2>Time</h2>
//                         <p className="predictedTime">10:09</p>
//                         <input type="submit" value="Get Time" id="buttonGetTime" className="submitButton"/>
//                     </div>
//                 </section>
//                 <footer>
//                     <p>pravega-ai &copy; 2020</p>
//                 </footer>
//             </div>
//         );
//     }
// }