// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iottwinmaker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::IoTTwinMaker::Scene
func LookupScene(ctx *pulumi.Context, args *LookupSceneArgs, opts ...pulumi.InvokeOption) (*LookupSceneResult, error) {
	var rv LookupSceneResult
	err := ctx.Invoke("aws-native:iottwinmaker:getScene", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSceneArgs struct {
	// The ID of the scene.
	SceneId string `pulumi:"sceneId"`
	// The ID of the scene.
	WorkspaceId string `pulumi:"workspaceId"`
}

type LookupSceneResult struct {
	// The ARN of the scene.
	Arn *string `pulumi:"arn"`
	// A list of capabilities that the scene uses to render.
	Capabilities []string `pulumi:"capabilities"`
	// The relative path that specifies the location of the content definition file.
	ContentLocation *string `pulumi:"contentLocation"`
	// The date and time when the scene was created.
	CreationDateTime *string `pulumi:"creationDateTime"`
	// The description of the scene.
	Description *string `pulumi:"description"`
	// A key-value pair of generated scene metadata for the scene.
	GeneratedSceneMetadata interface{} `pulumi:"generatedSceneMetadata"`
	// A key-value pair of scene metadata for the scene.
	SceneMetadata interface{} `pulumi:"sceneMetadata"`
	// A key-value pair to associate with a resource.
	Tags interface{} `pulumi:"tags"`
	// The date and time of the current update.
	UpdateDateTime *string `pulumi:"updateDateTime"`
}

func LookupSceneOutput(ctx *pulumi.Context, args LookupSceneOutputArgs, opts ...pulumi.InvokeOption) LookupSceneResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSceneResult, error) {
			args := v.(LookupSceneArgs)
			r, err := LookupScene(ctx, &args, opts...)
			var s LookupSceneResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSceneResultOutput)
}

type LookupSceneOutputArgs struct {
	// The ID of the scene.
	SceneId pulumi.StringInput `pulumi:"sceneId"`
	// The ID of the scene.
	WorkspaceId pulumi.StringInput `pulumi:"workspaceId"`
}

func (LookupSceneOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSceneArgs)(nil)).Elem()
}

type LookupSceneResultOutput struct{ *pulumi.OutputState }

func (LookupSceneResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSceneResult)(nil)).Elem()
}

func (o LookupSceneResultOutput) ToLookupSceneResultOutput() LookupSceneResultOutput {
	return o
}

func (o LookupSceneResultOutput) ToLookupSceneResultOutputWithContext(ctx context.Context) LookupSceneResultOutput {
	return o
}

// The ARN of the scene.
func (o LookupSceneResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSceneResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// A list of capabilities that the scene uses to render.
func (o LookupSceneResultOutput) Capabilities() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupSceneResult) []string { return v.Capabilities }).(pulumi.StringArrayOutput)
}

// The relative path that specifies the location of the content definition file.
func (o LookupSceneResultOutput) ContentLocation() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSceneResult) *string { return v.ContentLocation }).(pulumi.StringPtrOutput)
}

// The date and time when the scene was created.
func (o LookupSceneResultOutput) CreationDateTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSceneResult) *string { return v.CreationDateTime }).(pulumi.StringPtrOutput)
}

// The description of the scene.
func (o LookupSceneResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSceneResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// A key-value pair of generated scene metadata for the scene.
func (o LookupSceneResultOutput) GeneratedSceneMetadata() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupSceneResult) interface{} { return v.GeneratedSceneMetadata }).(pulumi.AnyOutput)
}

// A key-value pair of scene metadata for the scene.
func (o LookupSceneResultOutput) SceneMetadata() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupSceneResult) interface{} { return v.SceneMetadata }).(pulumi.AnyOutput)
}

// A key-value pair to associate with a resource.
func (o LookupSceneResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupSceneResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

// The date and time of the current update.
func (o LookupSceneResultOutput) UpdateDateTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSceneResult) *string { return v.UpdateDateTime }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSceneResultOutput{})
}
