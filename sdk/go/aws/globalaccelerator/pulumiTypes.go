// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package globalaccelerator

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

// Tag is a key-value pair associated with accelerator.
type AcceleratorTag struct {
	// Key of the tag. Value can be 1 to 127 characters.
	Key string `pulumi:"key"`
	// Value for the tag. Value can be 1 to 255 characters.
	Value string `pulumi:"value"`
}

// AcceleratorTagInput is an input type that accepts AcceleratorTagArgs and AcceleratorTagOutput values.
// You can construct a concrete instance of `AcceleratorTagInput` via:
//
//	AcceleratorTagArgs{...}
type AcceleratorTagInput interface {
	pulumi.Input

	ToAcceleratorTagOutput() AcceleratorTagOutput
	ToAcceleratorTagOutputWithContext(context.Context) AcceleratorTagOutput
}

// Tag is a key-value pair associated with accelerator.
type AcceleratorTagArgs struct {
	// Key of the tag. Value can be 1 to 127 characters.
	Key pulumi.StringInput `pulumi:"key"`
	// Value for the tag. Value can be 1 to 255 characters.
	Value pulumi.StringInput `pulumi:"value"`
}

func (AcceleratorTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AcceleratorTag)(nil)).Elem()
}

func (i AcceleratorTagArgs) ToAcceleratorTagOutput() AcceleratorTagOutput {
	return i.ToAcceleratorTagOutputWithContext(context.Background())
}

func (i AcceleratorTagArgs) ToAcceleratorTagOutputWithContext(ctx context.Context) AcceleratorTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AcceleratorTagOutput)
}

// AcceleratorTagArrayInput is an input type that accepts AcceleratorTagArray and AcceleratorTagArrayOutput values.
// You can construct a concrete instance of `AcceleratorTagArrayInput` via:
//
//	AcceleratorTagArray{ AcceleratorTagArgs{...} }
type AcceleratorTagArrayInput interface {
	pulumi.Input

	ToAcceleratorTagArrayOutput() AcceleratorTagArrayOutput
	ToAcceleratorTagArrayOutputWithContext(context.Context) AcceleratorTagArrayOutput
}

type AcceleratorTagArray []AcceleratorTagInput

func (AcceleratorTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AcceleratorTag)(nil)).Elem()
}

func (i AcceleratorTagArray) ToAcceleratorTagArrayOutput() AcceleratorTagArrayOutput {
	return i.ToAcceleratorTagArrayOutputWithContext(context.Background())
}

func (i AcceleratorTagArray) ToAcceleratorTagArrayOutputWithContext(ctx context.Context) AcceleratorTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AcceleratorTagArrayOutput)
}

// Tag is a key-value pair associated with accelerator.
type AcceleratorTagOutput struct{ *pulumi.OutputState }

func (AcceleratorTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AcceleratorTag)(nil)).Elem()
}

func (o AcceleratorTagOutput) ToAcceleratorTagOutput() AcceleratorTagOutput {
	return o
}

func (o AcceleratorTagOutput) ToAcceleratorTagOutputWithContext(ctx context.Context) AcceleratorTagOutput {
	return o
}

// Key of the tag. Value can be 1 to 127 characters.
func (o AcceleratorTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v AcceleratorTag) string { return v.Key }).(pulumi.StringOutput)
}

// Value for the tag. Value can be 1 to 255 characters.
func (o AcceleratorTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v AcceleratorTag) string { return v.Value }).(pulumi.StringOutput)
}

type AcceleratorTagArrayOutput struct{ *pulumi.OutputState }

func (AcceleratorTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AcceleratorTag)(nil)).Elem()
}

func (o AcceleratorTagArrayOutput) ToAcceleratorTagArrayOutput() AcceleratorTagArrayOutput {
	return o
}

func (o AcceleratorTagArrayOutput) ToAcceleratorTagArrayOutputWithContext(ctx context.Context) AcceleratorTagArrayOutput {
	return o
}

func (o AcceleratorTagArrayOutput) Index(i pulumi.IntInput) AcceleratorTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AcceleratorTag {
		return vs[0].([]AcceleratorTag)[vs[1].(int)]
	}).(AcceleratorTagOutput)
}

// The configuration for a given endpoint
type EndpointGroupEndpointConfiguration struct {
	// true if client ip should be preserved
	ClientIpPreservationEnabled *bool `pulumi:"clientIpPreservationEnabled"`
	// Id of the endpoint. For Network/Application Load Balancer this value is the ARN.  For EIP, this value is the allocation ID.  For EC2 instances, this is the EC2 instance ID
	EndpointId string `pulumi:"endpointId"`
	// The weight for the endpoint.
	Weight *int `pulumi:"weight"`
}

// EndpointGroupEndpointConfigurationInput is an input type that accepts EndpointGroupEndpointConfigurationArgs and EndpointGroupEndpointConfigurationOutput values.
// You can construct a concrete instance of `EndpointGroupEndpointConfigurationInput` via:
//
//	EndpointGroupEndpointConfigurationArgs{...}
type EndpointGroupEndpointConfigurationInput interface {
	pulumi.Input

	ToEndpointGroupEndpointConfigurationOutput() EndpointGroupEndpointConfigurationOutput
	ToEndpointGroupEndpointConfigurationOutputWithContext(context.Context) EndpointGroupEndpointConfigurationOutput
}

// The configuration for a given endpoint
type EndpointGroupEndpointConfigurationArgs struct {
	// true if client ip should be preserved
	ClientIpPreservationEnabled pulumi.BoolPtrInput `pulumi:"clientIpPreservationEnabled"`
	// Id of the endpoint. For Network/Application Load Balancer this value is the ARN.  For EIP, this value is the allocation ID.  For EC2 instances, this is the EC2 instance ID
	EndpointId pulumi.StringInput `pulumi:"endpointId"`
	// The weight for the endpoint.
	Weight pulumi.IntPtrInput `pulumi:"weight"`
}

func (EndpointGroupEndpointConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (i EndpointGroupEndpointConfigurationArgs) ToEndpointGroupEndpointConfigurationOutput() EndpointGroupEndpointConfigurationOutput {
	return i.ToEndpointGroupEndpointConfigurationOutputWithContext(context.Background())
}

func (i EndpointGroupEndpointConfigurationArgs) ToEndpointGroupEndpointConfigurationOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointGroupEndpointConfigurationOutput)
}

// EndpointGroupEndpointConfigurationArrayInput is an input type that accepts EndpointGroupEndpointConfigurationArray and EndpointGroupEndpointConfigurationArrayOutput values.
// You can construct a concrete instance of `EndpointGroupEndpointConfigurationArrayInput` via:
//
//	EndpointGroupEndpointConfigurationArray{ EndpointGroupEndpointConfigurationArgs{...} }
type EndpointGroupEndpointConfigurationArrayInput interface {
	pulumi.Input

	ToEndpointGroupEndpointConfigurationArrayOutput() EndpointGroupEndpointConfigurationArrayOutput
	ToEndpointGroupEndpointConfigurationArrayOutputWithContext(context.Context) EndpointGroupEndpointConfigurationArrayOutput
}

type EndpointGroupEndpointConfigurationArray []EndpointGroupEndpointConfigurationInput

func (EndpointGroupEndpointConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (i EndpointGroupEndpointConfigurationArray) ToEndpointGroupEndpointConfigurationArrayOutput() EndpointGroupEndpointConfigurationArrayOutput {
	return i.ToEndpointGroupEndpointConfigurationArrayOutputWithContext(context.Background())
}

func (i EndpointGroupEndpointConfigurationArray) ToEndpointGroupEndpointConfigurationArrayOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointGroupEndpointConfigurationArrayOutput)
}

// The configuration for a given endpoint
type EndpointGroupEndpointConfigurationOutput struct{ *pulumi.OutputState }

func (EndpointGroupEndpointConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (o EndpointGroupEndpointConfigurationOutput) ToEndpointGroupEndpointConfigurationOutput() EndpointGroupEndpointConfigurationOutput {
	return o
}

func (o EndpointGroupEndpointConfigurationOutput) ToEndpointGroupEndpointConfigurationOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationOutput {
	return o
}

// true if client ip should be preserved
func (o EndpointGroupEndpointConfigurationOutput) ClientIpPreservationEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v EndpointGroupEndpointConfiguration) *bool { return v.ClientIpPreservationEnabled }).(pulumi.BoolPtrOutput)
}

// Id of the endpoint. For Network/Application Load Balancer this value is the ARN.  For EIP, this value is the allocation ID.  For EC2 instances, this is the EC2 instance ID
func (o EndpointGroupEndpointConfigurationOutput) EndpointId() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointGroupEndpointConfiguration) string { return v.EndpointId }).(pulumi.StringOutput)
}

// The weight for the endpoint.
func (o EndpointGroupEndpointConfigurationOutput) Weight() pulumi.IntPtrOutput {
	return o.ApplyT(func(v EndpointGroupEndpointConfiguration) *int { return v.Weight }).(pulumi.IntPtrOutput)
}

type EndpointGroupEndpointConfigurationArrayOutput struct{ *pulumi.OutputState }

func (EndpointGroupEndpointConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointGroupEndpointConfiguration)(nil)).Elem()
}

func (o EndpointGroupEndpointConfigurationArrayOutput) ToEndpointGroupEndpointConfigurationArrayOutput() EndpointGroupEndpointConfigurationArrayOutput {
	return o
}

func (o EndpointGroupEndpointConfigurationArrayOutput) ToEndpointGroupEndpointConfigurationArrayOutputWithContext(ctx context.Context) EndpointGroupEndpointConfigurationArrayOutput {
	return o
}

func (o EndpointGroupEndpointConfigurationArrayOutput) Index(i pulumi.IntInput) EndpointGroupEndpointConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EndpointGroupEndpointConfiguration {
		return vs[0].([]EndpointGroupEndpointConfiguration)[vs[1].(int)]
	}).(EndpointGroupEndpointConfigurationOutput)
}

// listener to endpoint port mapping.
type EndpointGroupPortOverride struct {
	EndpointPort int `pulumi:"endpointPort"`
	ListenerPort int `pulumi:"listenerPort"`
}

// EndpointGroupPortOverrideInput is an input type that accepts EndpointGroupPortOverrideArgs and EndpointGroupPortOverrideOutput values.
// You can construct a concrete instance of `EndpointGroupPortOverrideInput` via:
//
//	EndpointGroupPortOverrideArgs{...}
type EndpointGroupPortOverrideInput interface {
	pulumi.Input

	ToEndpointGroupPortOverrideOutput() EndpointGroupPortOverrideOutput
	ToEndpointGroupPortOverrideOutputWithContext(context.Context) EndpointGroupPortOverrideOutput
}

// listener to endpoint port mapping.
type EndpointGroupPortOverrideArgs struct {
	EndpointPort pulumi.IntInput `pulumi:"endpointPort"`
	ListenerPort pulumi.IntInput `pulumi:"listenerPort"`
}

func (EndpointGroupPortOverrideArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointGroupPortOverride)(nil)).Elem()
}

func (i EndpointGroupPortOverrideArgs) ToEndpointGroupPortOverrideOutput() EndpointGroupPortOverrideOutput {
	return i.ToEndpointGroupPortOverrideOutputWithContext(context.Background())
}

func (i EndpointGroupPortOverrideArgs) ToEndpointGroupPortOverrideOutputWithContext(ctx context.Context) EndpointGroupPortOverrideOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointGroupPortOverrideOutput)
}

// EndpointGroupPortOverrideArrayInput is an input type that accepts EndpointGroupPortOverrideArray and EndpointGroupPortOverrideArrayOutput values.
// You can construct a concrete instance of `EndpointGroupPortOverrideArrayInput` via:
//
//	EndpointGroupPortOverrideArray{ EndpointGroupPortOverrideArgs{...} }
type EndpointGroupPortOverrideArrayInput interface {
	pulumi.Input

	ToEndpointGroupPortOverrideArrayOutput() EndpointGroupPortOverrideArrayOutput
	ToEndpointGroupPortOverrideArrayOutputWithContext(context.Context) EndpointGroupPortOverrideArrayOutput
}

type EndpointGroupPortOverrideArray []EndpointGroupPortOverrideInput

func (EndpointGroupPortOverrideArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointGroupPortOverride)(nil)).Elem()
}

func (i EndpointGroupPortOverrideArray) ToEndpointGroupPortOverrideArrayOutput() EndpointGroupPortOverrideArrayOutput {
	return i.ToEndpointGroupPortOverrideArrayOutputWithContext(context.Background())
}

func (i EndpointGroupPortOverrideArray) ToEndpointGroupPortOverrideArrayOutputWithContext(ctx context.Context) EndpointGroupPortOverrideArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointGroupPortOverrideArrayOutput)
}

// listener to endpoint port mapping.
type EndpointGroupPortOverrideOutput struct{ *pulumi.OutputState }

func (EndpointGroupPortOverrideOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointGroupPortOverride)(nil)).Elem()
}

func (o EndpointGroupPortOverrideOutput) ToEndpointGroupPortOverrideOutput() EndpointGroupPortOverrideOutput {
	return o
}

func (o EndpointGroupPortOverrideOutput) ToEndpointGroupPortOverrideOutputWithContext(ctx context.Context) EndpointGroupPortOverrideOutput {
	return o
}

func (o EndpointGroupPortOverrideOutput) EndpointPort() pulumi.IntOutput {
	return o.ApplyT(func(v EndpointGroupPortOverride) int { return v.EndpointPort }).(pulumi.IntOutput)
}

func (o EndpointGroupPortOverrideOutput) ListenerPort() pulumi.IntOutput {
	return o.ApplyT(func(v EndpointGroupPortOverride) int { return v.ListenerPort }).(pulumi.IntOutput)
}

type EndpointGroupPortOverrideArrayOutput struct{ *pulumi.OutputState }

func (EndpointGroupPortOverrideArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointGroupPortOverride)(nil)).Elem()
}

func (o EndpointGroupPortOverrideArrayOutput) ToEndpointGroupPortOverrideArrayOutput() EndpointGroupPortOverrideArrayOutput {
	return o
}

func (o EndpointGroupPortOverrideArrayOutput) ToEndpointGroupPortOverrideArrayOutputWithContext(ctx context.Context) EndpointGroupPortOverrideArrayOutput {
	return o
}

func (o EndpointGroupPortOverrideArrayOutput) Index(i pulumi.IntInput) EndpointGroupPortOverrideOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EndpointGroupPortOverride {
		return vs[0].([]EndpointGroupPortOverride)[vs[1].(int)]
	}).(EndpointGroupPortOverrideOutput)
}

// A port range to support for connections from  clients to your accelerator.
type ListenerPortRange struct {
	FromPort int `pulumi:"fromPort"`
	ToPort   int `pulumi:"toPort"`
}

// ListenerPortRangeInput is an input type that accepts ListenerPortRangeArgs and ListenerPortRangeOutput values.
// You can construct a concrete instance of `ListenerPortRangeInput` via:
//
//	ListenerPortRangeArgs{...}
type ListenerPortRangeInput interface {
	pulumi.Input

	ToListenerPortRangeOutput() ListenerPortRangeOutput
	ToListenerPortRangeOutputWithContext(context.Context) ListenerPortRangeOutput
}

// A port range to support for connections from  clients to your accelerator.
type ListenerPortRangeArgs struct {
	FromPort pulumi.IntInput `pulumi:"fromPort"`
	ToPort   pulumi.IntInput `pulumi:"toPort"`
}

func (ListenerPortRangeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ListenerPortRange)(nil)).Elem()
}

func (i ListenerPortRangeArgs) ToListenerPortRangeOutput() ListenerPortRangeOutput {
	return i.ToListenerPortRangeOutputWithContext(context.Background())
}

func (i ListenerPortRangeArgs) ToListenerPortRangeOutputWithContext(ctx context.Context) ListenerPortRangeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ListenerPortRangeOutput)
}

// ListenerPortRangeArrayInput is an input type that accepts ListenerPortRangeArray and ListenerPortRangeArrayOutput values.
// You can construct a concrete instance of `ListenerPortRangeArrayInput` via:
//
//	ListenerPortRangeArray{ ListenerPortRangeArgs{...} }
type ListenerPortRangeArrayInput interface {
	pulumi.Input

	ToListenerPortRangeArrayOutput() ListenerPortRangeArrayOutput
	ToListenerPortRangeArrayOutputWithContext(context.Context) ListenerPortRangeArrayOutput
}

type ListenerPortRangeArray []ListenerPortRangeInput

func (ListenerPortRangeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ListenerPortRange)(nil)).Elem()
}

func (i ListenerPortRangeArray) ToListenerPortRangeArrayOutput() ListenerPortRangeArrayOutput {
	return i.ToListenerPortRangeArrayOutputWithContext(context.Background())
}

func (i ListenerPortRangeArray) ToListenerPortRangeArrayOutputWithContext(ctx context.Context) ListenerPortRangeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ListenerPortRangeArrayOutput)
}

// A port range to support for connections from  clients to your accelerator.
type ListenerPortRangeOutput struct{ *pulumi.OutputState }

func (ListenerPortRangeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ListenerPortRange)(nil)).Elem()
}

func (o ListenerPortRangeOutput) ToListenerPortRangeOutput() ListenerPortRangeOutput {
	return o
}

func (o ListenerPortRangeOutput) ToListenerPortRangeOutputWithContext(ctx context.Context) ListenerPortRangeOutput {
	return o
}

func (o ListenerPortRangeOutput) FromPort() pulumi.IntOutput {
	return o.ApplyT(func(v ListenerPortRange) int { return v.FromPort }).(pulumi.IntOutput)
}

func (o ListenerPortRangeOutput) ToPort() pulumi.IntOutput {
	return o.ApplyT(func(v ListenerPortRange) int { return v.ToPort }).(pulumi.IntOutput)
}

type ListenerPortRangeArrayOutput struct{ *pulumi.OutputState }

func (ListenerPortRangeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ListenerPortRange)(nil)).Elem()
}

func (o ListenerPortRangeArrayOutput) ToListenerPortRangeArrayOutput() ListenerPortRangeArrayOutput {
	return o
}

func (o ListenerPortRangeArrayOutput) ToListenerPortRangeArrayOutputWithContext(ctx context.Context) ListenerPortRangeArrayOutput {
	return o
}

func (o ListenerPortRangeArrayOutput) Index(i pulumi.IntInput) ListenerPortRangeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ListenerPortRange {
		return vs[0].([]ListenerPortRange)[vs[1].(int)]
	}).(ListenerPortRangeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AcceleratorTagInput)(nil)).Elem(), AcceleratorTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AcceleratorTagArrayInput)(nil)).Elem(), AcceleratorTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EndpointGroupEndpointConfigurationInput)(nil)).Elem(), EndpointGroupEndpointConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*EndpointGroupEndpointConfigurationArrayInput)(nil)).Elem(), EndpointGroupEndpointConfigurationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*EndpointGroupPortOverrideInput)(nil)).Elem(), EndpointGroupPortOverrideArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*EndpointGroupPortOverrideArrayInput)(nil)).Elem(), EndpointGroupPortOverrideArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ListenerPortRangeInput)(nil)).Elem(), ListenerPortRangeArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ListenerPortRangeArrayInput)(nil)).Elem(), ListenerPortRangeArray{})
	pulumi.RegisterOutputType(AcceleratorTagOutput{})
	pulumi.RegisterOutputType(AcceleratorTagArrayOutput{})
	pulumi.RegisterOutputType(EndpointGroupEndpointConfigurationOutput{})
	pulumi.RegisterOutputType(EndpointGroupEndpointConfigurationArrayOutput{})
	pulumi.RegisterOutputType(EndpointGroupPortOverrideOutput{})
	pulumi.RegisterOutputType(EndpointGroupPortOverrideArrayOutput{})
	pulumi.RegisterOutputType(ListenerPortRangeOutput{})
	pulumi.RegisterOutputType(ListenerPortRangeArrayOutput{})
}
