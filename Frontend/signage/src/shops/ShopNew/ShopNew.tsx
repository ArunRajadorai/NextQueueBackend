import ShopForm, {
    FormModel,
    SetSubmitting,
} from '@/views/shops/ShopForm'
import toast from '@/components/ui/toast'
import Notification from '@/components/ui/Notification'
import { useNavigate } from 'react-router-dom'
import { apiCreateShop } from '@/services/ShopService'
// import axios from 'axios';
// import {apiCreateSalesProduct} from "@/services/SalesService";

const ShopNew = () => {
    const navigate = useNavigate()
    const addShop = async (data: FormModel) => {
         const response = await apiCreateShop<boolean, FormModel>(data)
    //    const response = await apiCreateShop(data)
         return response.data
    }
 const handleFormSubmit = async (
        values: FormModel,
        setSubmitting: SetSubmitting
    ) => {
        setSubmitting(true)
        const success = await addShop(values)
        setSubmitting(false)
        if (success) {
            toast.push(
                <Notification
                    title={'Successfully added'}
                    type="success"
                    duration={2500}
                >
                    Great!!Shop has been successfully added
                </Notification>,
                {
                    placement: 'top-center',
                }
            )
            navigate('/app/shops/shop-list')
        }
    }

    const handleDiscard = () => {
        navigate('/app/shops/shop-list')
    }

    return (
        <>
            <ShopForm
                type="new"
                onFormSubmit={handleFormSubmit}
                onDiscard={handleDiscard}
            />
        </>
    )
}

export default ShopNew
