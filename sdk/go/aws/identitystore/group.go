// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package identitystore

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::IdentityStore::Group
type Group struct {
	pulumi.CustomResourceState

	// A string containing the description of the group.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// A string containing the name of the group. This value is commonly displayed when the group is referenced.
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// The unique identifier for a group in the identity store.
	GroupId pulumi.StringOutput `pulumi:"groupId"`
	// The globally unique identifier for the identity store.
	IdentityStoreId pulumi.StringOutput `pulumi:"identityStoreId"`
}

// NewGroup registers a new resource with the given unique name, arguments, and options.
func NewGroup(ctx *pulumi.Context,
	name string, args *GroupArgs, opts ...pulumi.ResourceOption) (*Group, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DisplayName == nil {
		return nil, errors.New("invalid value for required argument 'DisplayName'")
	}
	if args.IdentityStoreId == nil {
		return nil, errors.New("invalid value for required argument 'IdentityStoreId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"identityStoreId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Group
	err := ctx.RegisterResource("aws-native:identitystore:Group", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGroup gets an existing Group resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GroupState, opts ...pulumi.ResourceOption) (*Group, error) {
	var resource Group
	err := ctx.ReadResource("aws-native:identitystore:Group", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Group resources.
type groupState struct {
}

type GroupState struct {
}

func (GroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*groupState)(nil)).Elem()
}

type groupArgs struct {
	// A string containing the description of the group.
	Description *string `pulumi:"description"`
	// A string containing the name of the group. This value is commonly displayed when the group is referenced.
	DisplayName string `pulumi:"displayName"`
	// The globally unique identifier for the identity store.
	IdentityStoreId string `pulumi:"identityStoreId"`
}

// The set of arguments for constructing a Group resource.
type GroupArgs struct {
	// A string containing the description of the group.
	Description pulumi.StringPtrInput
	// A string containing the name of the group. This value is commonly displayed when the group is referenced.
	DisplayName pulumi.StringInput
	// The globally unique identifier for the identity store.
	IdentityStoreId pulumi.StringInput
}

func (GroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*groupArgs)(nil)).Elem()
}

type GroupInput interface {
	pulumi.Input

	ToGroupOutput() GroupOutput
	ToGroupOutputWithContext(ctx context.Context) GroupOutput
}

func (*Group) ElementType() reflect.Type {
	return reflect.TypeOf((**Group)(nil)).Elem()
}

func (i *Group) ToGroupOutput() GroupOutput {
	return i.ToGroupOutputWithContext(context.Background())
}

func (i *Group) ToGroupOutputWithContext(ctx context.Context) GroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupOutput)
}

type GroupOutput struct{ *pulumi.OutputState }

func (GroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Group)(nil)).Elem()
}

func (o GroupOutput) ToGroupOutput() GroupOutput {
	return o
}

func (o GroupOutput) ToGroupOutputWithContext(ctx context.Context) GroupOutput {
	return o
}

// A string containing the description of the group.
func (o GroupOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// A string containing the name of the group. This value is commonly displayed when the group is referenced.
func (o GroupOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Group) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// The unique identifier for a group in the identity store.
func (o GroupOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *Group) pulumi.StringOutput { return v.GroupId }).(pulumi.StringOutput)
}

// The globally unique identifier for the identity store.
func (o GroupOutput) IdentityStoreId() pulumi.StringOutput {
	return o.ApplyT(func(v *Group) pulumi.StringOutput { return v.IdentityStoreId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GroupInput)(nil)).Elem(), &Group{})
	pulumi.RegisterOutputType(GroupOutput{})
}
