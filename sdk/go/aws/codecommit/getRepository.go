// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package codecommit

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::CodeCommit::Repository
func LookupRepository(ctx *pulumi.Context, args *LookupRepositoryArgs, opts ...pulumi.InvokeOption) (*LookupRepositoryResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRepositoryResult
	err := ctx.Invoke("aws-native:codecommit:getRepository", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRepositoryArgs struct {
	Id string `pulumi:"id"`
}

type LookupRepositoryResult struct {
	Arn                   *string             `pulumi:"arn"`
	CloneUrlHttp          *string             `pulumi:"cloneUrlHttp"`
	CloneUrlSsh           *string             `pulumi:"cloneUrlSsh"`
	Code                  *RepositoryCode     `pulumi:"code"`
	Id                    *string             `pulumi:"id"`
	KmsKeyId              *string             `pulumi:"kmsKeyId"`
	Name                  *string             `pulumi:"name"`
	RepositoryDescription *string             `pulumi:"repositoryDescription"`
	RepositoryName        *string             `pulumi:"repositoryName"`
	Tags                  []RepositoryTag     `pulumi:"tags"`
	Triggers              []RepositoryTrigger `pulumi:"triggers"`
}

func LookupRepositoryOutput(ctx *pulumi.Context, args LookupRepositoryOutputArgs, opts ...pulumi.InvokeOption) LookupRepositoryResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRepositoryResult, error) {
			args := v.(LookupRepositoryArgs)
			r, err := LookupRepository(ctx, &args, opts...)
			var s LookupRepositoryResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRepositoryResultOutput)
}

type LookupRepositoryOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupRepositoryOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRepositoryArgs)(nil)).Elem()
}

type LookupRepositoryResultOutput struct{ *pulumi.OutputState }

func (LookupRepositoryResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRepositoryResult)(nil)).Elem()
}

func (o LookupRepositoryResultOutput) ToLookupRepositoryResultOutput() LookupRepositoryResultOutput {
	return o
}

func (o LookupRepositoryResultOutput) ToLookupRepositoryResultOutputWithContext(ctx context.Context) LookupRepositoryResultOutput {
	return o
}

func (o LookupRepositoryResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupRepositoryResult] {
	return pulumix.Output[LookupRepositoryResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupRepositoryResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) CloneUrlHttp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.CloneUrlHttp }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) CloneUrlSsh() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.CloneUrlSsh }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) Code() RepositoryCodePtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *RepositoryCode { return v.Code }).(RepositoryCodePtrOutput)
}

func (o LookupRepositoryResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) RepositoryDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.RepositoryDescription }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) RepositoryName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRepositoryResult) *string { return v.RepositoryName }).(pulumi.StringPtrOutput)
}

func (o LookupRepositoryResultOutput) Tags() RepositoryTagArrayOutput {
	return o.ApplyT(func(v LookupRepositoryResult) []RepositoryTag { return v.Tags }).(RepositoryTagArrayOutput)
}

func (o LookupRepositoryResultOutput) Triggers() RepositoryTriggerArrayOutput {
	return o.ApplyT(func(v LookupRepositoryResult) []RepositoryTrigger { return v.Triggers }).(RepositoryTriggerArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRepositoryResultOutput{})
}
