// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package groundstation

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS Ground Station DataflowEndpointGroup schema for CloudFormation
type DataflowEndpointGroup struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
	ContactPostPassDurationSeconds pulumi.IntPtrOutput `pulumi:"contactPostPassDurationSeconds"`
	// Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
	ContactPrePassDurationSeconds pulumi.IntPtrOutput                             `pulumi:"contactPrePassDurationSeconds"`
	EndpointDetails               DataflowEndpointGroupEndpointDetailsArrayOutput `pulumi:"endpointDetails"`
	Tags                          DataflowEndpointGroupTagArrayOutput             `pulumi:"tags"`
}

// NewDataflowEndpointGroup registers a new resource with the given unique name, arguments, and options.
func NewDataflowEndpointGroup(ctx *pulumi.Context,
	name string, args *DataflowEndpointGroupArgs, opts ...pulumi.ResourceOption) (*DataflowEndpointGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EndpointDetails == nil {
		return nil, errors.New("invalid value for required argument 'EndpointDetails'")
	}
	var resource DataflowEndpointGroup
	err := ctx.RegisterResource("aws-native:groundstation:DataflowEndpointGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataflowEndpointGroup gets an existing DataflowEndpointGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataflowEndpointGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataflowEndpointGroupState, opts ...pulumi.ResourceOption) (*DataflowEndpointGroup, error) {
	var resource DataflowEndpointGroup
	err := ctx.ReadResource("aws-native:groundstation:DataflowEndpointGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataflowEndpointGroup resources.
type dataflowEndpointGroupState struct {
}

type DataflowEndpointGroupState struct {
}

func (DataflowEndpointGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataflowEndpointGroupState)(nil)).Elem()
}

type dataflowEndpointGroupArgs struct {
	// Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
	ContactPostPassDurationSeconds *int `pulumi:"contactPostPassDurationSeconds"`
	// Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
	ContactPrePassDurationSeconds *int                                   `pulumi:"contactPrePassDurationSeconds"`
	EndpointDetails               []DataflowEndpointGroupEndpointDetails `pulumi:"endpointDetails"`
	Tags                          []DataflowEndpointGroupTag             `pulumi:"tags"`
}

// The set of arguments for constructing a DataflowEndpointGroup resource.
type DataflowEndpointGroupArgs struct {
	// Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
	ContactPostPassDurationSeconds pulumi.IntPtrInput
	// Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
	ContactPrePassDurationSeconds pulumi.IntPtrInput
	EndpointDetails               DataflowEndpointGroupEndpointDetailsArrayInput
	Tags                          DataflowEndpointGroupTagArrayInput
}

func (DataflowEndpointGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataflowEndpointGroupArgs)(nil)).Elem()
}

type DataflowEndpointGroupInput interface {
	pulumi.Input

	ToDataflowEndpointGroupOutput() DataflowEndpointGroupOutput
	ToDataflowEndpointGroupOutputWithContext(ctx context.Context) DataflowEndpointGroupOutput
}

func (*DataflowEndpointGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**DataflowEndpointGroup)(nil)).Elem()
}

func (i *DataflowEndpointGroup) ToDataflowEndpointGroupOutput() DataflowEndpointGroupOutput {
	return i.ToDataflowEndpointGroupOutputWithContext(context.Background())
}

func (i *DataflowEndpointGroup) ToDataflowEndpointGroupOutputWithContext(ctx context.Context) DataflowEndpointGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataflowEndpointGroupOutput)
}

type DataflowEndpointGroupOutput struct{ *pulumi.OutputState }

func (DataflowEndpointGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataflowEndpointGroup)(nil)).Elem()
}

func (o DataflowEndpointGroupOutput) ToDataflowEndpointGroupOutput() DataflowEndpointGroupOutput {
	return o
}

func (o DataflowEndpointGroupOutput) ToDataflowEndpointGroupOutputWithContext(ctx context.Context) DataflowEndpointGroupOutput {
	return o
}

func (o DataflowEndpointGroupOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *DataflowEndpointGroup) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.
func (o DataflowEndpointGroupOutput) ContactPostPassDurationSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DataflowEndpointGroup) pulumi.IntPtrOutput { return v.ContactPostPassDurationSeconds }).(pulumi.IntPtrOutput)
}

// Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.
func (o DataflowEndpointGroupOutput) ContactPrePassDurationSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DataflowEndpointGroup) pulumi.IntPtrOutput { return v.ContactPrePassDurationSeconds }).(pulumi.IntPtrOutput)
}

func (o DataflowEndpointGroupOutput) EndpointDetails() DataflowEndpointGroupEndpointDetailsArrayOutput {
	return o.ApplyT(func(v *DataflowEndpointGroup) DataflowEndpointGroupEndpointDetailsArrayOutput {
		return v.EndpointDetails
	}).(DataflowEndpointGroupEndpointDetailsArrayOutput)
}

func (o DataflowEndpointGroupOutput) Tags() DataflowEndpointGroupTagArrayOutput {
	return o.ApplyT(func(v *DataflowEndpointGroup) DataflowEndpointGroupTagArrayOutput { return v.Tags }).(DataflowEndpointGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataflowEndpointGroupInput)(nil)).Elem(), &DataflowEndpointGroup{})
	pulumi.RegisterOutputType(DataflowEndpointGroupOutput{})
}
