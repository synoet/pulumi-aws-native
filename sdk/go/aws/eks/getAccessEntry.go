// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package eks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// An object representing an Amazon EKS AccessEntry.
func LookupAccessEntry(ctx *pulumi.Context, args *LookupAccessEntryArgs, opts ...pulumi.InvokeOption) (*LookupAccessEntryResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAccessEntryResult
	err := ctx.Invoke("aws-native:eks:getAccessEntry", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAccessEntryArgs struct {
	// The cluster that the access entry is created for.
	ClusterName string `pulumi:"clusterName"`
	// The principal ARN that the access entry is created for.
	PrincipalArn string `pulumi:"principalArn"`
}

type LookupAccessEntryResult struct {
	// The ARN of the access entry.
	AccessEntryArn *string `pulumi:"accessEntryArn"`
	// An array of access policies that are associated with the access entry.
	AccessPolicies []AccessEntryAccessPolicy `pulumi:"accessPolicies"`
	// The Kubernetes groups that the access entry is associated with.
	KubernetesGroups []string `pulumi:"kubernetesGroups"`
	// An array of key-value pairs to apply to this resource.
	Tags []AccessEntryTag `pulumi:"tags"`
	// The Kubernetes user that the access entry is associated with.
	Username *string `pulumi:"username"`
}

func LookupAccessEntryOutput(ctx *pulumi.Context, args LookupAccessEntryOutputArgs, opts ...pulumi.InvokeOption) LookupAccessEntryResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAccessEntryResult, error) {
			args := v.(LookupAccessEntryArgs)
			r, err := LookupAccessEntry(ctx, &args, opts...)
			var s LookupAccessEntryResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAccessEntryResultOutput)
}

type LookupAccessEntryOutputArgs struct {
	// The cluster that the access entry is created for.
	ClusterName pulumi.StringInput `pulumi:"clusterName"`
	// The principal ARN that the access entry is created for.
	PrincipalArn pulumi.StringInput `pulumi:"principalArn"`
}

func (LookupAccessEntryOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAccessEntryArgs)(nil)).Elem()
}

type LookupAccessEntryResultOutput struct{ *pulumi.OutputState }

func (LookupAccessEntryResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAccessEntryResult)(nil)).Elem()
}

func (o LookupAccessEntryResultOutput) ToLookupAccessEntryResultOutput() LookupAccessEntryResultOutput {
	return o
}

func (o LookupAccessEntryResultOutput) ToLookupAccessEntryResultOutputWithContext(ctx context.Context) LookupAccessEntryResultOutput {
	return o
}

func (o LookupAccessEntryResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupAccessEntryResult] {
	return pulumix.Output[LookupAccessEntryResult]{
		OutputState: o.OutputState,
	}
}

// The ARN of the access entry.
func (o LookupAccessEntryResultOutput) AccessEntryArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAccessEntryResult) *string { return v.AccessEntryArn }).(pulumi.StringPtrOutput)
}

// An array of access policies that are associated with the access entry.
func (o LookupAccessEntryResultOutput) AccessPolicies() AccessEntryAccessPolicyArrayOutput {
	return o.ApplyT(func(v LookupAccessEntryResult) []AccessEntryAccessPolicy { return v.AccessPolicies }).(AccessEntryAccessPolicyArrayOutput)
}

// The Kubernetes groups that the access entry is associated with.
func (o LookupAccessEntryResultOutput) KubernetesGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupAccessEntryResult) []string { return v.KubernetesGroups }).(pulumi.StringArrayOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupAccessEntryResultOutput) Tags() AccessEntryTagArrayOutput {
	return o.ApplyT(func(v LookupAccessEntryResult) []AccessEntryTag { return v.Tags }).(AccessEntryTagArrayOutput)
}

// The Kubernetes user that the access entry is associated with.
func (o LookupAccessEntryResultOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAccessEntryResult) *string { return v.Username }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAccessEntryResultOutput{})
}
