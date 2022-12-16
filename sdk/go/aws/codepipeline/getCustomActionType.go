// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package codepipeline

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::CodePipeline::CustomActionType resource creates a custom action for activities that aren't included in the CodePipeline default actions, such as running an internally developed build process or a test suite. You can use these custom actions in the stage of a pipeline.
func LookupCustomActionType(ctx *pulumi.Context, args *LookupCustomActionTypeArgs, opts ...pulumi.InvokeOption) (*LookupCustomActionTypeResult, error) {
	var rv LookupCustomActionTypeResult
	err := ctx.Invoke("aws-native:codepipeline:getCustomActionType", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCustomActionTypeArgs struct {
	// The category of the custom action, such as a build action or a test action.
	Category string `pulumi:"category"`
	// The provider of the service used in the custom action, such as AWS CodeDeploy.
	Provider string `pulumi:"provider"`
	// The version identifier of the custom action.
	Version string `pulumi:"version"`
}

type LookupCustomActionTypeResult struct {
	Id *string `pulumi:"id"`
	// Any tags assigned to the custom action.
	Tags []CustomActionTypeTag `pulumi:"tags"`
}

func LookupCustomActionTypeOutput(ctx *pulumi.Context, args LookupCustomActionTypeOutputArgs, opts ...pulumi.InvokeOption) LookupCustomActionTypeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCustomActionTypeResult, error) {
			args := v.(LookupCustomActionTypeArgs)
			r, err := LookupCustomActionType(ctx, &args, opts...)
			var s LookupCustomActionTypeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCustomActionTypeResultOutput)
}

type LookupCustomActionTypeOutputArgs struct {
	// The category of the custom action, such as a build action or a test action.
	Category pulumi.StringInput `pulumi:"category"`
	// The provider of the service used in the custom action, such as AWS CodeDeploy.
	Provider pulumi.StringInput `pulumi:"provider"`
	// The version identifier of the custom action.
	Version pulumi.StringInput `pulumi:"version"`
}

func (LookupCustomActionTypeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomActionTypeArgs)(nil)).Elem()
}

type LookupCustomActionTypeResultOutput struct{ *pulumi.OutputState }

func (LookupCustomActionTypeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomActionTypeResult)(nil)).Elem()
}

func (o LookupCustomActionTypeResultOutput) ToLookupCustomActionTypeResultOutput() LookupCustomActionTypeResultOutput {
	return o
}

func (o LookupCustomActionTypeResultOutput) ToLookupCustomActionTypeResultOutputWithContext(ctx context.Context) LookupCustomActionTypeResultOutput {
	return o
}

func (o LookupCustomActionTypeResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomActionTypeResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Any tags assigned to the custom action.
func (o LookupCustomActionTypeResultOutput) Tags() CustomActionTypeTagArrayOutput {
	return o.ApplyT(func(v LookupCustomActionTypeResult) []CustomActionTypeTag { return v.Tags }).(CustomActionTypeTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCustomActionTypeResultOutput{})
}
