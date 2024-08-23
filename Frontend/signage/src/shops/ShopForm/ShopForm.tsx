import { forwardRef, useState } from 'react'
import { FormContainer } from '@/components/ui/Form'
import Button from '@/components/ui/Button'
import hooks from '@/components/ui/hooks'
import StickyFooter from '@/components/shared/StickyFooter'
import ConfirmDialog from '@/components/shared/ConfirmDialog'
import { Form, Formik, FormikProps } from 'formik'
import BasicInformationFields from './BasicInformationFields'
import ShopContactFields from './ShopContactFields'
import DropdownFields from './DropdownFields'
import ProductImages from './ProductImages'
import cloneDeep from 'lodash/cloneDeep'
import { HiOutlineTrash } from 'react-icons/hi'
import {AiOutlineDelete, AiOutlineSave} from 'react-icons/ai'
import * as Yup from 'yup'

// eslint-disable-next-line  @typescript-eslint/no-explicit-any
type FormikRef = FormikProps<any>

type InitialData = {

    shopName?: string
    shopOwnername?: string
    img?: string
    imgList?: {
        id: string
        name: string
        img: string
    }[]
    shopEmail?: string
    shopPhone?: string
    shopAddress1?: string
    shopAddress2?: string
    shopTown?: string
    shopPostalcode?: string
    shopState?: string
    shopCountry?: string

}

export type FormModel = Omit<InitialData, 'tags'> & {
    tags: { label: string; value: string }[] | string[]
}

export type SetSubmitting = (isSubmitting: boolean) => void

export type OnDeleteCallback = React.Dispatch<React.SetStateAction<boolean>>

type OnDelete = (callback: OnDeleteCallback) => void

type ShopForm = {
    initialData?: InitialData
    type: 'edit' | 'new'
    onDiscard?: () => void
    onDelete?: OnDelete
    onFormSubmit: (formData: FormModel, setSubmitting: SetSubmitting) => void
}

/*
const { useUniqueId } = hooks
*/

const validationSchema = Yup.object().shape({
    shopName: Yup.string().required('Shop Name Required'),
    shopOwnername: Yup.string().required('Owner/Manager Name Required'),
    shopEmail: Yup.string().required('Email Required'),
    shopPhone: Yup.string().required('Phone Required'),
    shopAddress1: Yup.string().required('Street Address Required'),
    shopTown: Yup.string().required('Town/City Required'),
    shopPostalcode: Yup.string().required('Postal Code Required'),
})

const DeleteProductButton = ({ onDelete }: { onDelete: OnDelete }) => {
    const [dialogOpen, setDialogOpen] = useState(false)

    const onConfirmDialogOpen = () => {
        setDialogOpen(true)
    }

    const onConfirmDialogClose = () => {
        setDialogOpen(false)
    }

    const handleConfirm = () => {
        onDelete?.(setDialogOpen)
    }

    return (
        <>
            <Button
                className="text-red-600"
                variant="plain"
                size="sm"
                icon={<HiOutlineTrash />}
                type="button"
                onClick={onConfirmDialogOpen}
            >
                Delete
            </Button>
            <ConfirmDialog
                isOpen={dialogOpen}
                type="danger"
                title="Delete Shop"
                confirmButtonColor="red-600"
                onClose={onConfirmDialogClose}
                onRequestClose={onConfirmDialogClose}
                onCancel={onConfirmDialogClose}
                onConfirm={handleConfirm}
            >
                <p>
                    Are you sure you want to delete this Shop? All record
                    related to this product will be deleted as well. This action
                    cannot be undone.
                </p>
            </ConfirmDialog>
        </>
    )
}

const ShopForm = forwardRef<FormikRef, ShopForm>((props, ref) => {
    const {
        type,
        initialData = {
                shopName: '',
    shopOwnername: '',
    img: '',
    imgList: [],
    shopEmail: '',
    shopPhone: '',
    shopAddress1: '',
    shopAddress2: '',
    shopTown: '',
    shopPostalcode: '',
    shopState: '',
    shopCountry: '',

        },
        onFormSubmit,
        onDiscard,
        onDelete,
    } = props

/*
    const newId = useUniqueId('product-')
*/

    return (
        <>
            <Formik

                innerRef={ref}
                initialValues={initialData}
                validationSchema={validationSchema}
                onSubmit={(values: FormModel, { setSubmitting }) => {
                    const formData = cloneDeep(values)
                    onFormSubmit?.(formData, setSubmitting)
                }}
            >
                {({ values, touched, errors, isSubmitting }) => (
                    <Form>
                        <FormContainer>
                            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
                                <div className="lg:col-span-2">
                                    <BasicInformationFields
                                        touched={touched}
                                        errors={errors}
                                    />
                                    <ShopContactFields
                                        touched={touched}
                                        errors={errors}
                                        values={values}
                                    />
                                    {/*<DropdownFields
                                        touched={touched}
                                        errors={errors}
                                        values={values}
                                    />*/}
                                </div>
                                {/*<div className="lg:col-span-1">
                                    <ProductImages values={values}/>
                                </div>*/}
                            </div>
                            <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 center">
                                <div className="lg:col-span-2">
                                    <StickyFooter
                                        className="-mx-8 px-8 flex items-center justify-between py-4"
                                        stickyClass="border-t bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700"
                                    >
                                        <div>
                                            {type === 'edit' && (
                                                <DeleteProductButton
                                                    onDelete={onDelete as OnDelete}
                                                />
                                            )}
                                        </div>
                                        <div className="md:flex items-center">
                                            <Button
                                                size="sm"
                                                variant="solid"
                                                className="ltr:mr-3 rtl:ml-3"
                                                type="button"
                                                icon={<AiOutlineDelete/>}
                                                onClick={() => onDiscard?.()}
                                            >
                                                Discard
                                            </Button>
                                            <Button
                                                size="sm"
                                                variant="solid"
                                                loading={isSubmitting}
                                                icon={<AiOutlineSave/>}
                                                type="submit"
                                            >
                                                Save
                                            </Button>
                                        </div>
                                    </StickyFooter>
                                </div>
                            </div>
                        </FormContainer>
                    </Form>
                    )}
            </Formik>
        </>
    )
})

ShopForm.displayName = 'ShopForm'

export default ShopForm
