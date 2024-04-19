import renderElapsedString from "../utils/helper";
export default function Timer(props){
    const elapsedString=renderElapsedString(props.elapsed);
    return (
        <div className=''>
            <div className=''>
                <div className=''>
                    {props.title}
                </div>
                <div className=''>
                    {props.project}
                </div>
                <div className=''>
                    <h2>
                        {elapsedString}
                    </h2>
                </div>
                <div className=''>
                    <span className=''>
                        <i className=''/>
                    </span>
                    <span className=''>
                        <i className=''/>
                    </span>
                </div>
            </div>
            <div className=''>
                Start
            </div>
        </div>
    );
}