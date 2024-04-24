import renderElapsedString from '../utils/helper';

export default function Timer(props) {
    const elapsedString = renderElapsedString(props.elapsed);
    return (
        <div className='flex justify-center'>
            <div className='bg-white shadow-md rounded-lg top-2 m-5 w-1/3'>
                <div className='p-4'>
                    <div className="text-xl">{props.title}</div>
                    <div className="text-gray-500">{props.project}</div>
                    <div className="text-center mt-4">
                        <h2>{elapsedString}</h2>
                    </div>
                    <div className='flex justify-end mt-4'>
                        <span className="mr-2">
                            <i className="fas fa-edit"></i>
                        </span>
                        <span>
                            <i className="fas fa trash"></i>
                        </span>
                    </div>
                </div>
                <button className="bg-blue-500 text-white px-4 py-2 roundedb-lg w-full">
                    Start
                </button>
            </div>
        </div>
    );
}