// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Glue::MLTransform
func LookupMlTransform(ctx *pulumi.Context, args *LookupMlTransformArgs, opts ...pulumi.InvokeOption) (*LookupMlTransformResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMlTransformResult
	err := ctx.Invoke("aws-native:glue:getMlTransform", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMlTransformArgs struct {
	Id string `pulumi:"id"`
}

type LookupMlTransformResult struct {
	Description         *string                         `pulumi:"description"`
	GlueVersion         *string                         `pulumi:"glueVersion"`
	Id                  *string                         `pulumi:"id"`
	MaxCapacity         *float64                        `pulumi:"maxCapacity"`
	MaxRetries          *int                            `pulumi:"maxRetries"`
	Name                *string                         `pulumi:"name"`
	NumberOfWorkers     *int                            `pulumi:"numberOfWorkers"`
	Role                *string                         `pulumi:"role"`
	Tags                interface{}                     `pulumi:"tags"`
	Timeout             *int                            `pulumi:"timeout"`
	TransformEncryption *MlTransformTransformEncryption `pulumi:"transformEncryption"`
	TransformParameters *MlTransformTransformParameters `pulumi:"transformParameters"`
	WorkerType          *string                         `pulumi:"workerType"`
}

func LookupMlTransformOutput(ctx *pulumi.Context, args LookupMlTransformOutputArgs, opts ...pulumi.InvokeOption) LookupMlTransformResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMlTransformResult, error) {
			args := v.(LookupMlTransformArgs)
			r, err := LookupMlTransform(ctx, &args, opts...)
			var s LookupMlTransformResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMlTransformResultOutput)
}

type LookupMlTransformOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupMlTransformOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMlTransformArgs)(nil)).Elem()
}

type LookupMlTransformResultOutput struct{ *pulumi.OutputState }

func (LookupMlTransformResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMlTransformResult)(nil)).Elem()
}

func (o LookupMlTransformResultOutput) ToLookupMlTransformResultOutput() LookupMlTransformResultOutput {
	return o
}

func (o LookupMlTransformResultOutput) ToLookupMlTransformResultOutputWithContext(ctx context.Context) LookupMlTransformResultOutput {
	return o
}

func (o LookupMlTransformResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupMlTransformResultOutput) GlueVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *string { return v.GlueVersion }).(pulumi.StringPtrOutput)
}

func (o LookupMlTransformResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupMlTransformResultOutput) MaxCapacity() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *float64 { return v.MaxCapacity }).(pulumi.Float64PtrOutput)
}

func (o LookupMlTransformResultOutput) MaxRetries() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *int { return v.MaxRetries }).(pulumi.IntPtrOutput)
}

func (o LookupMlTransformResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupMlTransformResultOutput) NumberOfWorkers() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *int { return v.NumberOfWorkers }).(pulumi.IntPtrOutput)
}

func (o LookupMlTransformResultOutput) Role() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *string { return v.Role }).(pulumi.StringPtrOutput)
}

func (o LookupMlTransformResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupMlTransformResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

func (o LookupMlTransformResultOutput) Timeout() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *int { return v.Timeout }).(pulumi.IntPtrOutput)
}

func (o LookupMlTransformResultOutput) TransformEncryption() MlTransformTransformEncryptionPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *MlTransformTransformEncryption { return v.TransformEncryption }).(MlTransformTransformEncryptionPtrOutput)
}

func (o LookupMlTransformResultOutput) TransformParameters() MlTransformTransformParametersPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *MlTransformTransformParameters { return v.TransformParameters }).(MlTransformTransformParametersPtrOutput)
}

func (o LookupMlTransformResultOutput) WorkerType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMlTransformResult) *string { return v.WorkerType }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMlTransformResultOutput{})
}
