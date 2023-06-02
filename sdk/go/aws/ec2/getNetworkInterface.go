// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::EC2::NetworkInterface resource creates network interface
func LookupNetworkInterface(ctx *pulumi.Context, args *LookupNetworkInterfaceArgs, opts ...pulumi.InvokeOption) (*LookupNetworkInterfaceResult, error) {
	var rv LookupNetworkInterfaceResult
	err := ctx.Invoke("aws-native:ec2:getNetworkInterface", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupNetworkInterfaceArgs struct {
	// Network interface id.
	Id string `pulumi:"id"`
}

type LookupNetworkInterfaceResult struct {
	// A description for the network interface.
	Description *string `pulumi:"description"`
	// If you have instances or ENIs that rely on the IPv6 address not changing, to avoid disrupting traffic to instances or ENIs, you can enable a primary IPv6 address. Enable this option to automatically assign an IPv6 associated with the ENI attached to your instance to be the primary IPv6 address. When you enable an IPv6 address to be a primary IPv6, you cannot disable it. Traffic will be routed to the primary IPv6 address until the instance is terminated or the ENI is detached. If you have multiple IPv6 addresses associated with an ENI and you enable a primary IPv6 address, the first IPv6 address associated with the ENI becomes the primary IPv6 address.
	EnablePrimaryIpv6 *bool `pulumi:"enablePrimaryIpv6"`
	// A list of security group IDs associated with this network interface.
	GroupSet []string `pulumi:"groupSet"`
	// Network interface id.
	Id *string `pulumi:"id"`
	// The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. To specify specific IPv6 addresses, use the Ipv6Addresses property and don't specify this property.
	Ipv6AddressCount *int `pulumi:"ipv6AddressCount"`
	// One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet to associate with the network interface. If you're specifying a number of IPv6 addresses, use the Ipv6AddressCount property and don't specify this property.
	Ipv6Addresses []NetworkInterfaceInstanceIpv6Address `pulumi:"ipv6Addresses"`
	// Returns the primary private IP address of the network interface.
	PrimaryPrivateIpAddress *string `pulumi:"primaryPrivateIpAddress"`
	// Assigns a list of private IP addresses to the network interface. You can specify a primary private IP address by setting the value of the Primary property to true in the PrivateIpAddressSpecification property. If you want EC2 to automatically assign private IP addresses, use the SecondaryPrivateIpAddressCount property and do not specify this property.
	PrivateIpAddresses []NetworkInterfacePrivateIpAddressSpecification `pulumi:"privateIpAddresses"`
	// The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses
	SecondaryPrivateIpAddressCount *int `pulumi:"secondaryPrivateIpAddressCount"`
	// Returns the secondary private IP addresses of the network interface.
	SecondaryPrivateIpAddresses []string `pulumi:"secondaryPrivateIpAddresses"`
	// Indicates whether traffic to or from the instance is validated.
	SourceDestCheck *bool `pulumi:"sourceDestCheck"`
	// An arbitrary set of tags (key-value pairs) for this network interface.
	Tags []NetworkInterfaceTag `pulumi:"tags"`
}

func LookupNetworkInterfaceOutput(ctx *pulumi.Context, args LookupNetworkInterfaceOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkInterfaceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNetworkInterfaceResult, error) {
			args := v.(LookupNetworkInterfaceArgs)
			r, err := LookupNetworkInterface(ctx, &args, opts...)
			var s LookupNetworkInterfaceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNetworkInterfaceResultOutput)
}

type LookupNetworkInterfaceOutputArgs struct {
	// Network interface id.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupNetworkInterfaceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkInterfaceArgs)(nil)).Elem()
}

type LookupNetworkInterfaceResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkInterfaceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkInterfaceResult)(nil)).Elem()
}

func (o LookupNetworkInterfaceResultOutput) ToLookupNetworkInterfaceResultOutput() LookupNetworkInterfaceResultOutput {
	return o
}

func (o LookupNetworkInterfaceResultOutput) ToLookupNetworkInterfaceResultOutputWithContext(ctx context.Context) LookupNetworkInterfaceResultOutput {
	return o
}

// A description for the network interface.
func (o LookupNetworkInterfaceResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// If you have instances or ENIs that rely on the IPv6 address not changing, to avoid disrupting traffic to instances or ENIs, you can enable a primary IPv6 address. Enable this option to automatically assign an IPv6 associated with the ENI attached to your instance to be the primary IPv6 address. When you enable an IPv6 address to be a primary IPv6, you cannot disable it. Traffic will be routed to the primary IPv6 address until the instance is terminated or the ENI is detached. If you have multiple IPv6 addresses associated with an ENI and you enable a primary IPv6 address, the first IPv6 address associated with the ENI becomes the primary IPv6 address.
func (o LookupNetworkInterfaceResultOutput) EnablePrimaryIpv6() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) *bool { return v.EnablePrimaryIpv6 }).(pulumi.BoolPtrOutput)
}

// A list of security group IDs associated with this network interface.
func (o LookupNetworkInterfaceResultOutput) GroupSet() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) []string { return v.GroupSet }).(pulumi.StringArrayOutput)
}

// Network interface id.
func (o LookupNetworkInterfaceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. To specify specific IPv6 addresses, use the Ipv6Addresses property and don't specify this property.
func (o LookupNetworkInterfaceResultOutput) Ipv6AddressCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) *int { return v.Ipv6AddressCount }).(pulumi.IntPtrOutput)
}

// One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet to associate with the network interface. If you're specifying a number of IPv6 addresses, use the Ipv6AddressCount property and don't specify this property.
func (o LookupNetworkInterfaceResultOutput) Ipv6Addresses() NetworkInterfaceInstanceIpv6AddressArrayOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) []NetworkInterfaceInstanceIpv6Address { return v.Ipv6Addresses }).(NetworkInterfaceInstanceIpv6AddressArrayOutput)
}

// Returns the primary private IP address of the network interface.
func (o LookupNetworkInterfaceResultOutput) PrimaryPrivateIpAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) *string { return v.PrimaryPrivateIpAddress }).(pulumi.StringPtrOutput)
}

// Assigns a list of private IP addresses to the network interface. You can specify a primary private IP address by setting the value of the Primary property to true in the PrivateIpAddressSpecification property. If you want EC2 to automatically assign private IP addresses, use the SecondaryPrivateIpAddressCount property and do not specify this property.
func (o LookupNetworkInterfaceResultOutput) PrivateIpAddresses() NetworkInterfacePrivateIpAddressSpecificationArrayOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) []NetworkInterfacePrivateIpAddressSpecification {
		return v.PrivateIpAddresses
	}).(NetworkInterfacePrivateIpAddressSpecificationArrayOutput)
}

// The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses
func (o LookupNetworkInterfaceResultOutput) SecondaryPrivateIpAddressCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) *int { return v.SecondaryPrivateIpAddressCount }).(pulumi.IntPtrOutput)
}

// Returns the secondary private IP addresses of the network interface.
func (o LookupNetworkInterfaceResultOutput) SecondaryPrivateIpAddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) []string { return v.SecondaryPrivateIpAddresses }).(pulumi.StringArrayOutput)
}

// Indicates whether traffic to or from the instance is validated.
func (o LookupNetworkInterfaceResultOutput) SourceDestCheck() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) *bool { return v.SourceDestCheck }).(pulumi.BoolPtrOutput)
}

// An arbitrary set of tags (key-value pairs) for this network interface.
func (o LookupNetworkInterfaceResultOutput) Tags() NetworkInterfaceTagArrayOutput {
	return o.ApplyT(func(v LookupNetworkInterfaceResult) []NetworkInterfaceTag { return v.Tags }).(NetworkInterfaceTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkInterfaceResultOutput{})
}
