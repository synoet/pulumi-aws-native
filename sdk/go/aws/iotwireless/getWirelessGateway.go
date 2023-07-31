// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotwireless

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Create and manage wireless gateways, including LoRa gateways.
func LookupWirelessGateway(ctx *pulumi.Context, args *LookupWirelessGatewayArgs, opts ...pulumi.InvokeOption) (*LookupWirelessGatewayResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupWirelessGatewayResult
	err := ctx.Invoke("aws-native:iotwireless:getWirelessGateway", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupWirelessGatewayArgs struct {
	// Id for Wireless Gateway. Returned upon successful create.
	Id string `pulumi:"id"`
}

type LookupWirelessGatewayResult struct {
	// Arn for Wireless Gateway. Returned upon successful create.
	Arn *string `pulumi:"arn"`
	// Description of Wireless Gateway.
	Description *string `pulumi:"description"`
	// Id for Wireless Gateway. Returned upon successful create.
	Id *string `pulumi:"id"`
	// The date and time when the most recent uplink was received.
	LastUplinkReceivedAt *string `pulumi:"lastUplinkReceivedAt"`
	// The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.
	LoRaWan *WirelessGatewayLoRaWANGateway `pulumi:"loRaWan"`
	// Name of Wireless Gateway.
	Name *string `pulumi:"name"`
	// A list of key-value pairs that contain metadata for the gateway.
	Tags []WirelessGatewayTag `pulumi:"tags"`
	// Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.
	ThingArn *string `pulumi:"thingArn"`
	// Thing Name. If there is a Thing created, this can be returned with a Get call.
	ThingName *string `pulumi:"thingName"`
}

func LookupWirelessGatewayOutput(ctx *pulumi.Context, args LookupWirelessGatewayOutputArgs, opts ...pulumi.InvokeOption) LookupWirelessGatewayResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWirelessGatewayResult, error) {
			args := v.(LookupWirelessGatewayArgs)
			r, err := LookupWirelessGateway(ctx, &args, opts...)
			var s LookupWirelessGatewayResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWirelessGatewayResultOutput)
}

type LookupWirelessGatewayOutputArgs struct {
	// Id for Wireless Gateway. Returned upon successful create.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupWirelessGatewayOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWirelessGatewayArgs)(nil)).Elem()
}

type LookupWirelessGatewayResultOutput struct{ *pulumi.OutputState }

func (LookupWirelessGatewayResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWirelessGatewayResult)(nil)).Elem()
}

func (o LookupWirelessGatewayResultOutput) ToLookupWirelessGatewayResultOutput() LookupWirelessGatewayResultOutput {
	return o
}

func (o LookupWirelessGatewayResultOutput) ToLookupWirelessGatewayResultOutputWithContext(ctx context.Context) LookupWirelessGatewayResultOutput {
	return o
}

// Arn for Wireless Gateway. Returned upon successful create.
func (o LookupWirelessGatewayResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Description of Wireless Gateway.
func (o LookupWirelessGatewayResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Id for Wireless Gateway. Returned upon successful create.
func (o LookupWirelessGatewayResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The date and time when the most recent uplink was received.
func (o LookupWirelessGatewayResultOutput) LastUplinkReceivedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *string { return v.LastUplinkReceivedAt }).(pulumi.StringPtrOutput)
}

// The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.
func (o LookupWirelessGatewayResultOutput) LoRaWan() WirelessGatewayLoRaWANGatewayPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *WirelessGatewayLoRaWANGateway { return v.LoRaWan }).(WirelessGatewayLoRaWANGatewayPtrOutput)
}

// Name of Wireless Gateway.
func (o LookupWirelessGatewayResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// A list of key-value pairs that contain metadata for the gateway.
func (o LookupWirelessGatewayResultOutput) Tags() WirelessGatewayTagArrayOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) []WirelessGatewayTag { return v.Tags }).(WirelessGatewayTagArrayOutput)
}

// Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.
func (o LookupWirelessGatewayResultOutput) ThingArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *string { return v.ThingArn }).(pulumi.StringPtrOutput)
}

// Thing Name. If there is a Thing created, this can be returned with a Get call.
func (o LookupWirelessGatewayResultOutput) ThingName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessGatewayResult) *string { return v.ThingName }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWirelessGatewayResultOutput{})
}
