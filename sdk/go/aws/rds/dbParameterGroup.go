// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::RDS::DBParameterGroup resource creates a custom parameter group for an RDS database family
type DbParameterGroup struct {
	pulumi.CustomResourceState

	// Specifies the name of the DB parameter group
	DbParameterGroupName pulumi.StringPtrOutput `pulumi:"dbParameterGroupName"`
	// Provides the customer-specified description for this DB parameter group.
	Description pulumi.StringOutput `pulumi:"description"`
	// The DB parameter group family name.
	Family pulumi.StringOutput `pulumi:"family"`
	// An array of parameter names and values for the parameter update.
	Parameters pulumi.AnyOutput `pulumi:"parameters"`
	// An array of key-value pairs to apply to this resource.
	Tags DbParameterGroupTagArrayOutput `pulumi:"tags"`
}

// NewDbParameterGroup registers a new resource with the given unique name, arguments, and options.
func NewDbParameterGroup(ctx *pulumi.Context,
	name string, args *DbParameterGroupArgs, opts ...pulumi.ResourceOption) (*DbParameterGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.Family == nil {
		return nil, errors.New("invalid value for required argument 'Family'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DbParameterGroup
	err := ctx.RegisterResource("aws-native:rds:DbParameterGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDbParameterGroup gets an existing DbParameterGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDbParameterGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DbParameterGroupState, opts ...pulumi.ResourceOption) (*DbParameterGroup, error) {
	var resource DbParameterGroup
	err := ctx.ReadResource("aws-native:rds:DbParameterGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DbParameterGroup resources.
type dbParameterGroupState struct {
}

type DbParameterGroupState struct {
}

func (DbParameterGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbParameterGroupState)(nil)).Elem()
}

type dbParameterGroupArgs struct {
	// Specifies the name of the DB parameter group
	DbParameterGroupName *string `pulumi:"dbParameterGroupName"`
	// Provides the customer-specified description for this DB parameter group.
	Description string `pulumi:"description"`
	// The DB parameter group family name.
	Family string `pulumi:"family"`
	// An array of parameter names and values for the parameter update.
	Parameters interface{} `pulumi:"parameters"`
	// An array of key-value pairs to apply to this resource.
	Tags []DbParameterGroupTag `pulumi:"tags"`
}

// The set of arguments for constructing a DbParameterGroup resource.
type DbParameterGroupArgs struct {
	// Specifies the name of the DB parameter group
	DbParameterGroupName pulumi.StringPtrInput
	// Provides the customer-specified description for this DB parameter group.
	Description pulumi.StringInput
	// The DB parameter group family name.
	Family pulumi.StringInput
	// An array of parameter names and values for the parameter update.
	Parameters pulumi.Input
	// An array of key-value pairs to apply to this resource.
	Tags DbParameterGroupTagArrayInput
}

func (DbParameterGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbParameterGroupArgs)(nil)).Elem()
}

type DbParameterGroupInput interface {
	pulumi.Input

	ToDbParameterGroupOutput() DbParameterGroupOutput
	ToDbParameterGroupOutputWithContext(ctx context.Context) DbParameterGroupOutput
}

func (*DbParameterGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**DbParameterGroup)(nil)).Elem()
}

func (i *DbParameterGroup) ToDbParameterGroupOutput() DbParameterGroupOutput {
	return i.ToDbParameterGroupOutputWithContext(context.Background())
}

func (i *DbParameterGroup) ToDbParameterGroupOutputWithContext(ctx context.Context) DbParameterGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DbParameterGroupOutput)
}

type DbParameterGroupOutput struct{ *pulumi.OutputState }

func (DbParameterGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DbParameterGroup)(nil)).Elem()
}

func (o DbParameterGroupOutput) ToDbParameterGroupOutput() DbParameterGroupOutput {
	return o
}

func (o DbParameterGroupOutput) ToDbParameterGroupOutputWithContext(ctx context.Context) DbParameterGroupOutput {
	return o
}

// Specifies the name of the DB parameter group
func (o DbParameterGroupOutput) DbParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbParameterGroup) pulumi.StringPtrOutput { return v.DbParameterGroupName }).(pulumi.StringPtrOutput)
}

// Provides the customer-specified description for this DB parameter group.
func (o DbParameterGroupOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *DbParameterGroup) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The DB parameter group family name.
func (o DbParameterGroupOutput) Family() pulumi.StringOutput {
	return o.ApplyT(func(v *DbParameterGroup) pulumi.StringOutput { return v.Family }).(pulumi.StringOutput)
}

// An array of parameter names and values for the parameter update.
func (o DbParameterGroupOutput) Parameters() pulumi.AnyOutput {
	return o.ApplyT(func(v *DbParameterGroup) pulumi.AnyOutput { return v.Parameters }).(pulumi.AnyOutput)
}

// An array of key-value pairs to apply to this resource.
func (o DbParameterGroupOutput) Tags() DbParameterGroupTagArrayOutput {
	return o.ApplyT(func(v *DbParameterGroup) DbParameterGroupTagArrayOutput { return v.Tags }).(DbParameterGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DbParameterGroupInput)(nil)).Elem(), &DbParameterGroup{})
	pulumi.RegisterOutputType(DbParameterGroupOutput{})
}
