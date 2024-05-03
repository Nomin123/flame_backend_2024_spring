import { renderElapsedString } from '../utils/helper'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTrash, faPenToSquare } from '@fortawesome/free-solid-svg-icons'


export default function Timer({ title, project, elapsed, runningSince, onEditClick, onTrashClick, id }) {
    const elapsedString = renderElapsedString(elapsed)
    const handleTrashClick = () => {
        onTrashClick(id)
        console.log("delete", id)
    }
    return (
        <div className='flex justify-center'>
            <div className='bg-white shadow-md rounded-lg top-2 m-5 w-1/3'>
                <div className='p-4'>
                    <div className="text-xl">{title}</div>
                    <div className="text-gray-500">{project}</div>
                    <div className="text-center mt-4">
                        <h2>{elapsedString}</h2>
                    </div>
                    <div className='flex justify-end mt-4'>
                        <span className="mr-2" onClick={onEditClick}>
                           <FontAwesomeIcon icon={faPenToSquare} />
                        </span>
                        <span onClick={handleTrashClick}>
                            <FontAwesomeIcon icon={faTrash} />
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