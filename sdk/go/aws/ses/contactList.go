// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ses

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::SES::ContactList.
type ContactList struct {
	pulumi.CustomResourceState

	// The name of the contact list.
	ContactListName pulumi.StringPtrOutput `pulumi:"contactListName"`
	// The description of the contact list.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The tags (keys and values) associated with the contact list.
	Tags ContactListTagArrayOutput `pulumi:"tags"`
	// The topics associated with the contact list.
	Topics ContactListTopicArrayOutput `pulumi:"topics"`
}

// NewContactList registers a new resource with the given unique name, arguments, and options.
func NewContactList(ctx *pulumi.Context,
	name string, args *ContactListArgs, opts ...pulumi.ResourceOption) (*ContactList, error) {
	if args == nil {
		args = &ContactListArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"contactListName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ContactList
	err := ctx.RegisterResource("aws-native:ses:ContactList", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetContactList gets an existing ContactList resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetContactList(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ContactListState, opts ...pulumi.ResourceOption) (*ContactList, error) {
	var resource ContactList
	err := ctx.ReadResource("aws-native:ses:ContactList", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ContactList resources.
type contactListState struct {
}

type ContactListState struct {
}

func (ContactListState) ElementType() reflect.Type {
	return reflect.TypeOf((*contactListState)(nil)).Elem()
}

type contactListArgs struct {
	// The name of the contact list.
	ContactListName *string `pulumi:"contactListName"`
	// The description of the contact list.
	Description *string `pulumi:"description"`
	// The tags (keys and values) associated with the contact list.
	Tags []ContactListTag `pulumi:"tags"`
	// The topics associated with the contact list.
	Topics []ContactListTopic `pulumi:"topics"`
}

// The set of arguments for constructing a ContactList resource.
type ContactListArgs struct {
	// The name of the contact list.
	ContactListName pulumi.StringPtrInput
	// The description of the contact list.
	Description pulumi.StringPtrInput
	// The tags (keys and values) associated with the contact list.
	Tags ContactListTagArrayInput
	// The topics associated with the contact list.
	Topics ContactListTopicArrayInput
}

func (ContactListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*contactListArgs)(nil)).Elem()
}

type ContactListInput interface {
	pulumi.Input

	ToContactListOutput() ContactListOutput
	ToContactListOutputWithContext(ctx context.Context) ContactListOutput
}

func (*ContactList) ElementType() reflect.Type {
	return reflect.TypeOf((**ContactList)(nil)).Elem()
}

func (i *ContactList) ToContactListOutput() ContactListOutput {
	return i.ToContactListOutputWithContext(context.Background())
}

func (i *ContactList) ToContactListOutputWithContext(ctx context.Context) ContactListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContactListOutput)
}

type ContactListOutput struct{ *pulumi.OutputState }

func (ContactListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ContactList)(nil)).Elem()
}

func (o ContactListOutput) ToContactListOutput() ContactListOutput {
	return o
}

func (o ContactListOutput) ToContactListOutputWithContext(ctx context.Context) ContactListOutput {
	return o
}

// The name of the contact list.
func (o ContactListOutput) ContactListName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ContactList) pulumi.StringPtrOutput { return v.ContactListName }).(pulumi.StringPtrOutput)
}

// The description of the contact list.
func (o ContactListOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ContactList) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The tags (keys and values) associated with the contact list.
func (o ContactListOutput) Tags() ContactListTagArrayOutput {
	return o.ApplyT(func(v *ContactList) ContactListTagArrayOutput { return v.Tags }).(ContactListTagArrayOutput)
}

// The topics associated with the contact list.
func (o ContactListOutput) Topics() ContactListTopicArrayOutput {
	return o.ApplyT(func(v *ContactList) ContactListTopicArrayOutput { return v.Topics }).(ContactListTopicArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ContactListInput)(nil)).Elem(), &ContactList{})
	pulumi.RegisterOutputType(ContactListOutput{})
}
