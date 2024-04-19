export default function TimerForm(props) {

    const submitText = props.title ? 'Update' : 'Create';
    return (
        <div className=''>
            <div className="">
                <div className="">
                    <div className="">
                        <label >Title</label>
                        <input type="text" defaultValue={props.title} />
                    </div>
                    <div className="">
                        <label >Project</label>
                        <input type="text" defaultValue={props.project} />
                    </div>
                    <div className="">
                        <button className="">
                            {submitText}
                        </button>
                        <button className="">
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}